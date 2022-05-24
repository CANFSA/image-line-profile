# Standard library imports
from pathlib import Path
# Third-party imports (need to pip install)
import imageio as iio
import matplotlib.pyplot as plt
import numpy as np
from skimage import measure


def plot_img_and_line(img, line_pt0, line_pt1, ums_per_pixel, fig_w=7):
    profile = measure.profile_line(
        img, line_pt0, line_pt1, mode='nearest'
    )
    profile_length = ums_per_pixel * np.arange(0, len(profile))
    profile_norm = (profile - np.mean(profile)) / np.std(profile)
    # Setup plot
    nrows = 1
    ncols = 2
    img_w = img.shape[1]
    img_h = img.shape[0]
    fig_h = fig_w * (img_h / img_w) * (nrows / ncols)
    fig, axes = plt.subplots(
        nrows=nrows, ncols=ncols, figsize=(fig_w, fig_h), dpi=150, 
        constrained_layout=True, facecolor='white'
    )
    axes[0].imshow(img, cmap='gray')
    axes[0].set_axis_off()
    axes[0].plot([line_pt0[0], line_pt1[0]], [line_pt0[1], line_pt1[1]])
    axes[1].plot(
        profile_length,
        profile,
        label='Raw radiograph intensity'
    )
    # axes[1].plot(
    #     profile_length,
    #     profile_norm,
    #     label='Normalized radiograph intensity'
    # )
    # axes[1].legend()
    return fig, axes

# This block is run if file executed as script
if __name__ == '__main__':
    # Load image
    img_dir = Path(r'example-imgs/')
    if not img_dir.exists():
        print('Directory not found')
    img_paths = [path for path in img_dir.glob('*.tif')]
    img = iio.imread(img_paths[0])
    # Plot image and intenisty
    ums_per_pixel = 2  # Dummy value
    fig, axes = plot_img_and_line(img, (250, 250), (500, 500), ums_per_pixel)
    plt.show()

