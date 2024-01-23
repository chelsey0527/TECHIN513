import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Define the triangle waveform function
def triangle_wave(t):
    # Triangle wave with peak at 1 and support between -1 and 1
    return np.clip(1 - np.abs(t), a_min=0, a_max=None)

# Define the rectangular pulse function, positioned from 0 to 5 on the time axis
def rectangular_pulse(t):
    # Rectangular pulse of height 4
    return 4 * (np.heaviside(t, 1) - np.heaviside(t - 5, 1))

# Generate time points for the evaluation
time_points = np.linspace(-7, 7, 1000)

# Calculate the waveforms at the generated time points
triangle_values = triangle_wave(time_points)
rectangular_values = rectangular_pulse(time_points)

# Plot the triangle waveform F(t)
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.plot(time_points, triangle_values, label='Triangle Waveform F(t)')
plt.title("Triangle Waveform F(t)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot the rectangular pulse G(t)
plt.subplot(1, 2, 2)
plt.plot(time_points, rectangular_values, color='red', label='Rectangular Pulse G(t)')
plt.title("Rectangular Pulse G(t)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Perform convolution between the triangle waveform and the rectangular pulse
conv_result = convolve(triangle_values, rectangular_values, mode='full')
# Normalize the convolution result for better comparison
conv_result /= np.max(conv_result)
# Establish a new time axis for the convolution result
time_convolution = np.linspace(time_points[0] + time_points[0], time_points[-1] + time_points[-1], len(conv_result))

# Plot the normalized convolution result
plt.figure(figsize=(14, 4))
plt.plot(time_convolution, conv_result, color='green', label='Convolution Result')
plt.title("Normalized Convolution of F(t) and Flipped G(t)")
plt.xlabel("Time (t)")
plt.ylabel("Normalized Amplitude")
plt.grid(True)
plt.legend()
plt.show()
