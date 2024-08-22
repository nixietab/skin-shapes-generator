import os
import random
from PIL import Image, ImageDraw

SKIN_SIZE = (64, 64)
OUTPUT_DIRECTORY = "generated_skins"
SKIN_NAME = "skin.png"

def generate_minecraft_skin():
    skin = Image.new("RGBA", SKIN_SIZE, (0, 0, 0, 0))
    
    head_top = generate_part((8, 8))
    head_bottom = generate_part((8, 8))
    head_front = generate_part((8, 8), add_eyes=True)
    head_back = generate_part((8, 8))
    head_left = generate_part((8, 8))
    head_right = generate_part((8, 8))

    body_front = generate_part((8, 12))
    body_back = generate_part((8, 12))
    body_left = generate_part((4, 12))
    body_right = generate_part((4, 12))

    arm_left_top = generate_part((4, 4))
    arm_left_bottom = generate_part((4, 4))
    arm_left_front = generate_part((4, 12))
    arm_left_back = generate_part((4, 12))
    arm_left_outer = generate_part((4, 12))
    arm_left_inner = generate_part((4, 12))

    arm_right_top = arm_left_top.copy()
    arm_right_bottom = arm_left_bottom.copy()
    arm_right_front = arm_left_front.copy()
    arm_right_back = arm_left_back.copy()
    arm_right_outer = arm_left_outer.copy()
    arm_right_inner = arm_left_inner.copy()

    leg_left_top = generate_part((4, 4))
    leg_left_bottom = generate_part((4, 4))
    leg_left_front = generate_part((4, 12))
    leg_left_back = generate_part((4, 12))
    leg_left_outer = generate_part((4, 12))
    leg_left_inner = generate_part((4, 12))

    leg_right_top = leg_left_top.copy()
    leg_right_bottom = leg_left_bottom.copy()
    leg_right_front = leg_left_front.copy()
    leg_right_back = leg_left_back.copy()
    leg_right_outer = leg_left_outer.copy()
    leg_right_inner = leg_left_inner.copy()

    parts_positions = {
        # Head
        "head_top": ((8, 0), head_top),
        "head_bottom": ((16, 0), head_bottom),
        "head_front": ((8, 8), head_front),
        "head_back": ((24, 8), head_back),
        "head_left": ((16, 8), head_left),
        "head_right": ((0, 8), head_right),
        
        # Body
        "body_front": ((20, 20), body_front),
        "body_back": ((32, 20), body_back),
        "body_left": ((16, 20), body_left),
        "body_right": ((28, 20), body_right),
        
        # Left Arm
        "arm_left_top": ((48, 0), arm_left_top),
        "arm_left_bottom": ((52, 0), arm_left_bottom),
        "arm_left_front": ((44, 20), arm_left_front),
        "arm_left_back": ((56, 20), arm_left_back),
        "arm_left_outer": ((52, 20), arm_left_outer),
        "arm_left_inner": ((48, 20), arm_left_inner),
        
        # Right Arm
        "arm_right_top": ((44, 0), arm_right_top),
        "arm_right_bottom": ((48, 0), arm_right_bottom),
        "arm_right_front": ((36, 52), arm_right_front),
        "arm_right_back": ((48, 52), arm_right_back),
        "arm_right_outer": ((40, 52), arm_right_outer),
        "arm_right_inner": ((44, 52), arm_right_inner),
        
        # Left Leg
        "leg_left_top": ((4, 0), leg_left_top),
        "leg_left_bottom": ((8, 0), leg_left_bottom),
        "leg_left_front": ((4, 20), leg_left_front),
        "leg_left_back": ((12, 20), leg_left_back),
        "leg_left_outer": ((8, 20), leg_left_outer),
        "leg_left_inner": ((0, 20), leg_left_inner),
        
        # Right Leg
        "leg_right_top": ((20, 48), leg_right_top),
        "leg_right_bottom": ((24, 48), leg_right_bottom),
        "leg_right_front": ((20, 20), leg_right_front),
        "leg_right_back": ((28, 20), leg_right_back),
        "leg_right_outer": ((24, 20), leg_right_outer),
        "leg_right_inner": ((16, 20), leg_right_inner),
    }
    
    # Paste each part into the skin template
    for coords, part in parts_positions.values():
        skin.paste(part, coords)
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    skin_path = os.path.join(OUTPUT_DIRECTORY, SKIN_NAME)
    counter = 1
    while os.path.exists(skin_path):
        skin_name, skin_ext = os.path.splitext(SKIN_NAME)
        skin_path = os.path.join(OUTPUT_DIRECTORY, f"{skin_name}_{counter}{skin_ext}")
        counter += 1
    
    skin.save(skin_path, "PNG")
    print(f"Skin Generated!: {skin_path}")

def generate_part(size, add_eyes=False):
    part = Image.new("RGBA", size, (0, 0, 0, 255))
    draw = ImageDraw.Draw(part)
    
    min_shapes = 3  # Minimum number of shapes to ensure coverage
    max_shapes = 6  # Maximum number of shapes for variety
    
    num_shapes = random.randint(min_shapes, max_shapes)
    for _ in range(num_shapes):
        shape_type = random.choice(["rectangle", "ellipse", "polygon"])
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            255  # Full opacity
        )
        if shape_type == "rectangle":
            x1 = random.randint(0, size[0] - 2)
            y1 = random.randint(0, size[1] - 2)
            x2 = random.randint(x1 + 1, size[0] - 1)
            y2 = random.randint(y1 + 1, size[1] - 1)
            draw.rectangle([x1, y1, x2, y2], fill=color)
        elif shape_type == "ellipse":
            x1 = random.randint(0, size[0] - 2)
            y1 = random.randint(0, size[1] - 2)
            x2 = random.randint(x1 + 1, size[0] - 1)
            y2 = random.randint(y1 + 1, size[1] - 1)
            draw.ellipse([x1, y1, x2, y2], fill=color)
        elif shape_type == "polygon":
            points = [
                (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1)) for _ in range(3)
            ]
            draw.polygon(points, fill=color)
    
    if add_eyes and size == (8, 8):
        draw_eyes(draw)
    
    return part

def draw_eyes(draw):
    eye_color = (255, 255, 255, 255)  # White color
    # Left Eye
    draw.rectangle([(1, 2), (2, 3)], fill=eye_color)
    # Right Eye
    draw.rectangle([(5, 2), (6, 3)], fill=eye_color)

if __name__ == "__main__":
    generate_minecraft_skin()
