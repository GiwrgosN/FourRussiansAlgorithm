# Four Russians Algorithm

Implementation of FourRussiansAlgorithm for matrix multiplication  and complementary graph using Python

The main idea of the method is to partition the matrix into small square blocks of size t × t for some parameter t, and to use a lookup table to perform the algorithm quickly within each block. The index into the lookup table encodes the values of the matrix cells on the upper left of the block boundary prior to some operation of the algorithm, and the result of the lookup table encodes the values of the boundary cells on the lower right of the block after the operation. Thus, the overall algorithm may be performed by operating on only (n/t)^2 blocks instead of on n^2 matrix cells, where n is the side length of the matrix. In order to keep the size of the lookup tables (and the time needed to initialize them) sufficiently small, t is typically chosen to be O(log n).

