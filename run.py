#!/usr/bin/env python3
from typical_set.typical_set import AEP
from typical_set.visual_utils import * 

if __name__ == "__main__":
    seed = 42 # random seed 
    p = 0.4 # probability of a being 1 
    n = 1000 # size of the random sequence 
    min_m = 10 # maximum number of random sequences
    max_m = 101_000 # intial number of random sequences 
    step_m = 1000 # step, larger steps will run faster 
    duration = 200 # duration per frame in the gif 
    hist_path = "./plots" # Path for a temporary directory where to save plots 
    save_hist(n, max_m, min_m, step_m, hist_path, p, seed) # Save figures to ./plots defined in visual_utils.py
    gen_gif(max_m, min_m, step_m, duration, hist_path)   # generate a gif from the plots defined in visual_utils.py
    remove_plots(max_m, min_m, step_m) # Remove the remporary folder ./plots 
 
