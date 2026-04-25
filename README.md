# Power Grid Optimization — Jupyter Notebook Series

> **Author**: Xinyu Li · Carnegie Mellon University, Dept. of Chemical Engineering  
> **Research Group**: Center for Advanced Process Decision-Making (CAPD)  
> **Status**: Active development (PhD research notes, open for community use)

A research-level, self-contained collection of Jupyter notebooks covering the theory and computational practice of **power grid optimization** — from classical LP/NLP foundations through AC-OPF, unit commitment, PTDF-based market analysis, and beyond.

The style is inspired by [Prof. John Kitchin's open course notebooks](https://github.com/jkitchin/s26-06643): each notebook is readable as a standalone document, combines derivations with working code, and builds on the previous ones.

---

## 📚 Notebook Series

| # | Topic | Key Tools | Status |
|---|-------|-----------|--------|
| [01](notebooks/01-optimization-foundations.ipynb) | Optimization Foundations — LP, NLP, MILP, MINLP | Pyomo, GLPK, IPOPT | ✅ |
| [02](notebooks/02-solver-algorithms.ipynb) | Solver Algorithms — KKT, IPM, Branch-and-Bound | Pyomo, IPOPT | ✅ |
| [03](notebooks/03-power-flow-models.ipynb) | Power Flow Models — π-model, DC & AC power flow | NumPy, SciPy | ✅ |
| [04](notebooks/04-dc-opf.ipynb) | DC Optimal Power Flow | Pyomo, GLPK | 🚧 |
| [05](notebooks/05-ac-opf.ipynb) | AC Optimal Power Flow | Pyomo, Egret, IPOPT | 🚧 |
| [06](notebooks/06-unit-commitment.ipynb) | Unit Commitment (UC + ACOPF) | Pyomo, Gurobi/GLPK | 🚧 |
| [07](notebooks/07-relaxations.ipynb) | Relaxations & Approximations of AC-OPF | Pyomo, CVXPY | 🚧 |
| [08](notebooks/08-ptdf-lodf.ipynb) | PTDF, LODF & N-1 Contingency Analysis | NumPy | 🚧 |
| [09](notebooks/09-electricity-markets.ipynb) | Electricity Markets, LMP & FTR Portfolio | Pyomo | 🚧 |
| [10](notebooks/10-ml-for-opf.ipynb) | Machine Learning for OPF (warm-start, active sets) | PyTorch, scikit-learn | 📋 |

**Legend**: ✅ Complete · 🚧 In progress · 📋 Planned

---

## 🗺 Learning Path

```
Optimization Foundations (01)
        │
        ▼
Solver Algorithms (02)
        │
        ▼
Power Flow Models (03)
     ┌──┴──┐
     ▼     ▼
DC-OPF   AC-OPF
  (04)    (05)
     │     │
     └──┬──┘
        ▼
 Unit Commitment (06)
        │
   ┌────┼────┐
   ▼    ▼    ▼
Relax PTDF  Markets
 (07)  (08)   (09)
              │
              ▼
         ML for OPF (10)
```

---

## 🛠 Installation

### Prerequisites
- Anaconda or Miniconda
- Git

### Setup

```bash
git clone https://github.com/Xyli2024/power-grid-optimization.git
cd power-grid-optimization
conda env create -f environment.yml
conda activate pgopt
jupyter lab
```

### Solvers

The notebooks use open-source solvers by default:
- **IPOPT** (nonlinear): installed via `conda-forge`
- **GLPK** (linear/MILP): installed via `conda-forge`
- **HiGHS** (linear): installed via `highspy`

For large-scale problems, [Gurobi](https://www.gurobi.com/academia/academic-program-and-licenses/) (free academic license) and [HSL linear solvers](https://licences.rock-inst.rl.ac.uk/account/login) for IPOPT are recommended.

---

## 📂 Repository Structure

```
power-grid-optimization/
├── notebooks/          # Main notebook series (01–10)
├── data/
│   ├── ieee14/         # IEEE 14-bus test case
│   ├── ieee30/         # IEEE 30-bus test case
│   └── ieee118/        # IEEE 118-bus test case
├── utils/              # Shared helper functions
│   └── network.py      # Network data loading utilities
├── environment.yml     # Conda environment specification
└── README.md
```

---

## 🔑 Key References

- Zimmerman, R. D., Murillo-Sánchez, C. E., & Thomas, R. J. (2011). MATPOWER. *IEEE Trans. Power Systems*.
- Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge University Press.
- Molzahn, D. K., & Hiskens, I. A. (2019). A survey of relaxations and approximations of the power flow equations. *Foundations and Trends in Electric Energy Systems*.
- Apostolopoulou, D. (2013). *Optimized FTR Portfolio Construction: The Speculator's Problem*. University of Illinois.
- Hart, W. E. et al. (2017). *Pyomo — Optimization Modeling in Python* (2nd ed.). Springer.

---

## 📝 License

MIT License — feel free to use, adapt, and share with attribution.

---

## 🤝 Contributing

This is primarily personal research notes, but issues and PRs are welcome. If you spot an error in a derivation or have a better code example, please open an issue.
