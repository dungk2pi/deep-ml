import numpy as np

def calculate_contrast(img) -> int:
	max = img[0][0]
	min = img[0][0]
	for row in img:
		for pixel in row:
			if pixel > max:
				max = pixel
			if pixel < min:
				min = pixel

	return max - min
