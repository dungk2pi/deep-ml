def calculate_brightness(img: list[list[int]]) -> float:
    if img is None or len(img) == 0:
        return -1

    row_len = len(img[0])
    if row_len == 0 or any(len(row) != row_len for row in img):
        return -1

    total = 0
    count = 0
    for row in img:
        for pixel in row:
            if 0 <= pixel <= 255:
                total += pixel
                count += 1
            else:
                return -1

    return total / count