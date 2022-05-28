# Four Russians Algorithm

## Implementation of Four Russians Algorithm for matrix multiplication  and complementary graph using Python

The main idea of the method is to partition the matrix into small square blocks of size t × t for some parameter t, and to use a lookup table to perform the algorithm quickly within each block. The index into the lookup table encodes the values of the matrix cells on the upper left of the block boundary prior to some operation of the algorithm, and the result of the lookup table encodes the values of the boundary cells on the lower right of the block after the operation. Thus, the overall algorithm may be performed by operating on only (n/t)^2 blocks instead of on n^2 matrix cells, where n is the side length of the matrix. In order to keep the size of the lookup tables (and the time needed to initialize them) sufficiently small, t is typically chosen to be O(log n).

** Below we can see the Pseudocode of the algorithm **

![image](https://user-images.githubusercontent.com/43292736/170828760-36e56a58-fce5-4462-92ca-3c036c5b54d8.png)

For more info about the details of this project please check: https://nbviewer.org/github/dmst-algorithms-course/assignment-2017-4/blob/master/assignment-2017-4.ipynb?flush_cache=true&fbclid=IwAR13_SA2A_7jf2kvUzbeiB5rxkkWOG4b9AwhFd_tHXN09A3blifFs0wjiY4
