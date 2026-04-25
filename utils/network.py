"""
utils/network.py
----------------
Lightweight helper functions for loading and inspecting power system
test cases used throughout the notebook series.

Supported formats:
- pandapower built-in networks (ieee case4gs, case14, case30, case118, ...)
- pypower case dict
"""

import numpy as np


# ---------------------------------------------------------------------------
# pandapower loaders
# ---------------------------------------------------------------------------

def load_pandapower_case(name: str):
    """
    Load a standard IEEE test case via pandapower.

    Parameters
    ----------
    name : str
        One of 'case4gs', 'case5', 'case14', 'case30', 'case39',
        'case57', 'case118', 'case300', etc.

    Returns
    -------
    net : pandapower.pandapowerNet
    """
    import pandapower.networks as ppnet
    loader = getattr(ppnet, name, None)
    if loader is None:
        raise ValueError(f"Unknown pandapower case: '{name}'. "
                         f"See pandapower.networks for available cases.")
    return loader()


def net_summary(net) -> None:
    """Print a quick summary of a pandapower network."""
    print(f"Buses     : {len(net.bus)}")
    print(f"Lines     : {len(net.line)}")
    print(f"Generators: {len(net.gen) + len(net.sgen) + len(net.ext_grid)}")
    print(f"Loads     : {len(net.load)}")
    print(f"Shunts    : {len(net.shunt)}")
    if hasattr(net, 'trafo'):
        print(f"Trafo     : {len(net.trafo)}")


# ---------------------------------------------------------------------------
# pypower loaders (used in some Pyomo notebooks)
# ---------------------------------------------------------------------------

def load_pypower_case(name: str) -> dict:
    """
    Load a PYPOWER case dict.

    Parameters
    ----------
    name : str  e.g. 'case14', 'case30', 'case118'

    Returns
    -------
    ppc : dict with keys 'bus', 'gen', 'branch', 'gencost', 'baseMVA'
    """
    import importlib
    try:
        mod = importlib.import_module(f"pypower.case{name.replace('case', '')}")
        loader = getattr(mod, name)
        return loader()
    except (ImportError, AttributeError) as e:
        raise ValueError(f"Could not load pypower case '{name}': {e}")


# ---------------------------------------------------------------------------
# PTDF utilities (used in notebook 08)
# ---------------------------------------------------------------------------

def build_ptdf(B_bus: np.ndarray, A: np.ndarray, slack: int = 0) -> np.ndarray:
    """
    Compute the Power Transfer Distribution Factor (PTDF) matrix.

    Parameters
    ----------
    B_bus : (n, n) array   Nodal susceptance matrix (DC approximation)
    A     : (l, n) array   Branch-node incidence matrix (±1 entries)
    slack : int            Index of the slack/reference bus

    Returns
    -------
    PTDF : (l, n) array    PTDF[line, bus] = fraction of 1 MW injected at
                            bus that flows on line.
    """
    n = B_bus.shape[0]
    l = A.shape[0]

    # Remove slack row/col to get reduced system
    keep = [i for i in range(n) if i != slack]
    B_red = B_bus[np.ix_(keep, keep)]
    A_red = A[:, keep]

    # B_red * theta = p_inj  =>  theta = B_red^{-1} p_inj
    B_inv = np.linalg.inv(B_red)

    # PTDF_red[line, bus_reduced] = b_line * (A_red @ B_inv)[line, bus]
    b_line = A_red @ B_inv          # (l, n-1)

    # Reconstruct full matrix (slack column stays zero)
    PTDF = np.zeros((l, n))
    for col_idx, bus_idx in enumerate(keep):
        PTDF[:, bus_idx] = b_line[:, col_idx]

    return PTDF
