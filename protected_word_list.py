# Words for which an exact match only should be capitalized.
# Usually 1 letter "words" that are actually symbols.
#
# This searches for an EXACT word match.
list_of_dangerous_words = [
    'I', 'V', 'X', 'C', 'T', 'B',
]
# In this list, if a match is found, the first letter should be capitalized.
# It will also replace the plural version of the word.
#
# This does NOT seach for an exact match, but rather a substring match.
list_of_first_letter_capitalized_words = [
    'B\\\'ezier', 'C++', 'B-spline', 'T-spline', 'B-Patch',
]
# Words that usually have a suffix, or maybe a prefix.
# If a match is found, the word will be surrounded by {}, but not the suffix or prefix.
#
# This does NOT seach for an exact match, but rather a substring match.
list_of_replaceable_words = [
    'NACA', 'RAE', 'ONERA', 'CRM',
]

# Words for which an exact match only should be capitalized.
#
# This searches for an EXACT word match.
list_of_capitalized_words = [
    'Newton', 'Gauss', 'Seidel', 'Laplace', 'Euler', 'Lagrange', 'Hamilton', 'Poisson',
    'Fourier', 'Laguerre', 'Hermite', 'Bessel', 'Legendre', 'Chebyshev', 'Bernstein',
    'Gegenbauer', 'Jacobi', 'Sturm', 'Liouville', 'Dirichlet', 'Neumann',
    'Cauchy', 'Riemann', 'Weierstrass', 'Hilbert', 'Galois', 'Noether',
    'Navier', 'Stokes', 'Einstein', 'Boltzmann', 'Planck', 'Heisenberg',
    'Lobatto', 'Schur', 'Lanczos', 'Krylov', 'Arnoldi', 'Gram', 'Schmidt',
    'Lagrangian', 'Eulerian', 
    'Sylvester',
    'GMRES', 'BICGSTAB', 'CGS', 'QMR', 'TFQMR', 'MINRES', 'LSQR',
    'Cuthill', 'McKee', 'RCM', 'METIS', 'ParMETIS', 'SCOTCH',
    'FEM', 'FDM', 'FVM', 'FMM', 'FE', 'DG', 'DPG', 'SUPG', 'CDG', 'NFEM', 'XFEM', 'RKDG', 'DGMPM', 'DGSEM', 'NEFEM',
    'PDE', 'ODE', 'BVP', 'IVP',
    'PDEs', 'ODEs', 'BVPs', 'IVPs',
    'CFD', 'RANS', 'LES', 'DNS', 'LBM', 'DES', 'VLES', 'VMS',  'DNS',
    'CFL', 'Mach', 'Reynolds', 'Prandtl', 'Schmidt', 'Peclet', 'Strouhal',
    'MPI', 'OpenMP', 'CUDA', 'OpenACC', 'OpenCL', 'SYCL', 'HIP', 'ROCm',
    'Python', 'Fortran', 'Julia', 'MATLAB', 'GNU', 'Linux',
    'FLOPS', 'GFLOPS', 'TFLOPS',
    'MacOS', 'Windows', 'Unix', 'BSD', 'OpenBSD', 'FreeBSD', 'NetBSD',
    'Galerkin', 'Petrov', 
    'Monte', 'Carlo',
    'Runge', 'Kutta', 'Lax', 'Wendroff', 'Friedrichs', 
    'Roe', 'Harten', 'Leer', 'Osher', 'Chakravarthy',
    'TVB', 'TVD', 'MUSCL', 'Albada', 'HLL', 'HLLC', 'HLLD', 'Rusanov', 
    'SQP', 'QP', 'LP', 'QP', 'SOCP', 'SDP', 'MILP', 'MIP', 'MIQP', 'MIQCQP',
    'GPU', 'CPU', 'TPU', 'FPGA', 'ASIC', 'GPGPU', 'SIMD', 'SIMT', 'SIMT',
    'WENO', 'HWENO', 'ENO',
    'BLAS', 'LAPACK', 'MKL', 'ATLAS', 'OpenBLAS', 'cuBLAS', 'cuSPARSE',
    'CAD', 'NURBS', 'Bezier', 'NURCCs',
    '1D', '2D', '3D',
    'II', 'III', 'IV',
    'VI', 'VII', 'VIII', 'IX',
    'BFGS', 'L-BFGS', 'CG', 'GD', 'SGD', 'ADAM', 'RMSProp', 'NAG', 'LBFGS',
    'Hessian', 'Jacobian',
    'FUN3D', 'SU2', 'OpenFOAM', 'HYPRE', 'Hypre', 'MFEM', 'Nek5000', 
    'deal.II', 'FEniCS', 'libMesh', 'PETSc', 'SLEPc', 'Trilinos', 'MOOSE',
    'Sacado', 'CppAD', 'ADOL-C', 'ADIC', 'TAPENADE', 'ADIFOR', 'CoDiPack', 
    'SNOPT', 'NLPQLP', 'NLopt', 'IPOPT', 'KNITRO', 'NLPQL', 'SciCompKL',
    'Basel', 'PyFR', 'Ridge Rider', 'PHiLiP',
    'Ifpack', 'Epetra', 'Aztec', 'Amesos', 'Anasazi', 'Belos', 'MueLu', 'Zoltan', 'Isorropia', 'NOX', 'Piro', 
    'ROL', 'Rythmos', 'Stokhos', 'Stratimikos', 'Teuchos', 'Thyra', 'Tpetra', 'Xpetra', 'Zoltan2',
]