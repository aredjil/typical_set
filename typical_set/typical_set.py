#!/usr/bin/env python3
import numpy as np
class AEP:
    def __init__(self, sample_size: int, seq_size: int, p: float, seed:int=None):
        self._sample_size = sample_size
        self._seq_size = seq_size
        self._p = p
        if seed == None:
            np.random.seed(seed)
        self._seq_set = self._gen_bin_seqs()
        self._probs = self._compute_p()

    def _gen_bin_seqs(self):
        return np.random.choice([0, 1], size=(self._sample_size, self._seq_size), p=[1 - self._p, self._p])
    
    def _compute_p(self):
        seq_set = np.array(self._seq_set)
        ones_count = np.count_nonzero(seq_set, axis=1)
        
        p_seq = (self._p ** ones_count) * ((1 - self._p) ** (self._seq_size - ones_count))
        
        return p_seq
    def get_entropy(self):
        p = self._p
        if p == 0 or p == 1:
            return 0  
        return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

    def get_info_content(self):
        return -np.log2(self._probs) 
