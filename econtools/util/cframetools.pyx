cimport cython      #noqa
import numpy as np
cimport numpy as np  #noqa

@cython.boundscheck(False)
cdef np.ndarray[double, ndim=2] crossmap(np.ndarray s1, np.ndarray s2, f):
    cdef unsigned int n1, n2
    cdef unsigned int i, j
    n1 = s1.shape[0]
    n2 = s2.shape[0]
    cpdef np.ndarray[double, ndim=2] res = np.zeros([n1, n2])
    for i in range(n1):
        for j in range(n2):
            res[i, j] = f(s1[i], s2[j])
    return res


cpdef np.ndarray[double, ndim=2] demean(np.ndarray arr, np.ndarray g):
    cdef unsigned int I, J
    cdef np.ndarray[double, ndim=1] means
    cdef np.ndarray[double, ndim=2] demeaned
    means = arr.mean(axis=0)
    demeaned = arr - means
    return demeaned
