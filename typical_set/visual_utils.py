#!/usr/bin/env python3
import numpy as np 
import matplotlib.pyplot as plt 
from tqdm import tqdm
from PIL import Image 
import os 
from typical_set.typical_set import AEP

def create_gif(image_folder, output_path, m_range, duration=100):
    images = []
    try:
        os.makedirs(output_path, exist_ok=True)
        print(f"Created {output_path}")
    except Exception as e: 
        print(f"An execption occured {e}")
    try:
        print("Generating the GIF...")
        for m in m_range:
            file_name = f"plot_{m}.png"  
            file_path = os.path.join(image_folder, file_name)
            if os.path.exists(file_path):
                img = Image.open(file_path)
                images.append(img)
            else:
                print(f"File not found: {file_path}")
        
        if images:
            images[0].save(
                output_path+"/aep.gif",
                save_all=True,
                append_images=images[1:],  
                duration=duration  
            )
            print(f"GIF saved at {output_path}")
        else:
            print("No images were found to create a GIF.")
    except Exception as e:
        print(f"An error occurred: {e}")
def gen_gif(max_m:int, min_m:int, step_m:int, duration:int, hist_path:str):
    
    output_gif = "./gifs"  
    m_range = range(min_m, max_m, step_m) 
    duration_per_frame = duration  

    create_gif(hist_path, output_gif, m_range, duration=duration_per_frame)

def save_hist(n:int, max_m:int, min_m:int, step_m:int, hist_path:str, p:float, seed:int):
    try:
        os.makedirs(hist_path, exist_ok=True)
    except Exception as e: 
        print(f"An execption occured {e}")
    for m in tqdm(range(min_m, max_m, step_m), desc="Plotting..."):
        aep = AEP(m, n, p, 42)
        
        info_content = aep.get_info_content()
        
        bins = np.histogram_bin_edges(info_content, bins='auto')

        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))

        counts, bins, patches = ax.hist(info_content, bins=bins, density=True, color="#2ca25f")
        ax.axvline(aep.get_entropy() * n, color='red', linestyle='--', label='nH(X)')
        ax.set_ylim(0, max(counts) * 1.1) 
        # NOTE: LOWER BOUND SHOULD BE ADJUSTED if you are going to change p 
        # This value was choosen ad hoc to center the plot :p 
        ax.set_xlim(900, n+10)
        ax.set_title(f"\n {m} sequences \n sequence size = {n}\n p = {p}")
        ax.set_xlabel("Information Content (bits)")
        ax.set_ylabel("Frequency")
        ax.legend()


        # fig.suptitle(f"Information Content", fontsize=16) 
        plt.tight_layout()  
        plt.savefig(f"./{hist_path}/plot_{m}.png")

        plt.close(fig)

def remove_plots(max_m:int, min_m:int, step_m:int):
    hist_path = "./plots"
    for m in range(min_m, max_m, step_m):
        file_path = f"./{hist_path}/plot_{m}.png"
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e: 
                print(f"An error occured while removing {file_path} {e}")
    os.rmdir(hist_path)
    print(f"removed {hist_path}")