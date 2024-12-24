#!/usr/bin/env python3
from typical_set.typical_set import AEP
from typical_set.visual_utils import * 

if __name__ == "__main__":
    seed = 42 # random seed 
    p = 0.25 # probability of a being 1 
    n = 1000 # size of the random sequence 
    min_m = 10 # maximum number of random sequences
    max_m = 101_000 # intial number of random sequences 
    step_m = 1000 # step 
    duration = 200 # duration per frame in the gif 
    hist_path = "./plots"
    save_hist(n, max_m, min_m, step_m, hist_path, p, seed)
    gen_gif(max_m, min_m, step_m, duration, hist_path)   
    remove_plots(max_m, min_m, step_m)
 
