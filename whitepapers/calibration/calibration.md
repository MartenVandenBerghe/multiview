# Camera calibration

## Simplest case

Suppose that the following camera characteristics are known

- $f$ focal length (from camera datasheet)

- $\sigma_x, \sigma_y$: pixel densities (from camera datasheet)

- $o_X, o_Y$: crossing of optical axis and sensor plane, e.g. in the middle of the sensor

- lens distortion, e.g. negligible lens distortion

- pinhole camera model suffices

Then we need no calibration


## Slightly harder case

Suppose known:

- $o_X, o_Y$: crossing of optical axis and sensor plane, e.g. in the middle of the sensor

- lens distortion, e.g. negligible lens distortion

- pinhole camera model suffices
 
Suppose we want to find:

- $f$ focal length

- $\sigma_x, \sigma_y$: pixel densities

Method

- Place an object with clearly identifiable markers $a,b,c,...$ on the table.

- Make pictures from different camera positions $A,B,C,...$ (and store those positions).

- The absolute positions $\vec{X}_
{aA}, \vec{X}_{aB}$ of the markers in the WRF world reference frame) are unknown.

- The relative positions $\vec{X}_{aA} - \vec{X} _{aB}, ...$ of the markers between two shots are known and equal to the camera motion.

- The pixel positions $(p_{aA}, q_{aA}), (p_{aB}, q_{aB}), ...$ of the images on the sensor plane can be read from the images (manually or autmatically). 

If we apply the pinhole model for one marker $a$ and one camera position $A$


$$X = \begin{bmatrix}
1 & x_{1}\\
\1 & x_{2} \\
1 & x_{3}
\end{bmatrix}$$



