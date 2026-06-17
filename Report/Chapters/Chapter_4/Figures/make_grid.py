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


def make_grid(filenames, outname='combined_figure.png', figsize=(10, 10), dpi=300):
    missing = [f for f in filenames if not os.path.exists(f)]
    if missing:
        raise FileNotFoundError(f"Missing files: {missing}")

    imgs = [Image.open(f).convert('RGB') for f in filenames]

    fig, axes = plt.subplots(3, 2, figsize=figsize)
    axes = axes.flatten()

    for ax, img, fname in zip(axes, imgs, filenames):
        ax.imshow(img)
        # ax.set_title(os.path.basename(fname))
        ax.axis('off')

    plt.tight_layout()
    fig.savefig(outname, dpi=dpi, bbox_inches='tight')
    print(f"Saved {outname}")


if __name__ == '__main__':
    files = [
        'plot4_heatmap_target-te.png',
        'plot4_heatmap_target-th.png',
        'plot4_drift_heatmap_lang-te.png',
        'plot4_drift_heatmap_lang-th.png',
        'plot4_lineplot.png',
        'plot4_drift_lineplot.png'
    ]

    make_grid(files)
