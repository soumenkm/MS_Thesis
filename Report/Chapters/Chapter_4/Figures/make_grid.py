#!/usr/bin/env python3
"""
Create a 2x2 grid figure from four PNG images located in the same directory as this script.

Usage:
    python make_grid.py

Output:
    combined_figure.png
"""
from PIL import Image
import matplotlib.pyplot as plt
import os


def make_grid(filenames, outname='combined_figure.png', dpi=300):
    missing = [f for f in filenames if not os.path.exists(f)]
    if missing:
        raise FileNotFoundError(f"Missing files: {missing}")

    imgs = [Image.open(f).convert('RGB') for f in filenames]

    # Match figure aspect to the images (3 wide, 2 tall)
    w, h = imgs[0].size
    aspect = h / w
    fig_w = 15
    fig_h = fig_w / 3 * aspect * 2

    fig, axes = plt.subplots(2, 3, figsize=(fig_w, fig_h))
    axes = axes.flatten()

    for ax, img in zip(axes, imgs):
        ax.imshow(img)
        ax.axis('off')

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0.02, wspace=0.02)
    plt.savefig(outname, dpi=dpi, bbox_inches='tight', pad_inches=0.05)
    print(f"Saved {outname}")


if __name__ == '__main__':
    files = [
        'plot4_heatmap_target-te.png',
        'plot4_heatmap_target-th.png',
        'plot4_lineplot.png',
        'plot4_drift_heatmap_lang-te.png',
        'plot4_drift_heatmap_lang-th.png',
        'plot4_drift_lineplot.png'
    ]

    make_grid(files)
