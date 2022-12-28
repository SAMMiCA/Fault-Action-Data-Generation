import random
from PIL import Image

actions = ["MoveAhead", "MoveBack", "MoveLeft", "MoveRight", "RotateRight", "RotateLeft"]

def get_data_movement(controller, positions, normal, done_position_action_sets, TARGET_MOVE=0.25, TARGET_ROTATE=45, MIN_FAULT_DIST=0.03, MIN_ERROR_DIST_RATE=0.12, MIN_FAULT_DEGREE=5, MIN_ERROR_DEGREE_RATE=1/9):
    position = random.choice(positions)
    action = random.choice(actions)

    if normal:
        if 'Move' in action:
            mag = TARGET_MOVE
        elif 'Rotate' in action:
            deg = TARGET_ROTATE
    else:
        if 'Move' in action:
            while True:
                mag = round(random.uniform(0.01, 1.0),1)
                if mag < TARGET_MOVE - max(MIN_FAULT_DIST, TARGET_MOVE*MIN_ERROR_DIST_RATE) or TARGET_MOVE + max(MIN_FAULT_DIST, TARGET_MOVE*MIN_ERROR_DIST_RATE):
                    break
        elif 'Rotate' in action:
            while True:
                deg = round(random.uniform(0, 360))
                if deg < TARGET_ROTATE - max(MIN_FAULT_DEGREE, TARGET_ROTATE*MIN_ERROR_DEGREE_RATE) or TARGET_ROTATE + max(MIN_FAULT_DEGREE, TARGET_ROTATE*MIN_ERROR_DEGREE_RATE):
                    break
    
    state = False
    if (position, action) not in done_position_action_sets:
        controller.step(
            action="Teleport",
            position=position,
            rotation=dict(x=0, y=random.uniform(0, 360), z=0)
        )
        
        if controller.last_event.metadata['lastActionSuccess'] == True:
            img1 = Image.fromarray(controller.last_event.frame)
            
            if 'Move' in action:
                controller.step(
                    action = action,
                    moveMagnitude = mag
                )
            elif 'Rotate' in action:
                controller.step(
                    action = action,
                    degrees = deg
                )
            
            if controller.last_event.metadata['lastActionSuccess'] == True:
                img2 = Image.fromarray(controller.last_event.frame)
                state = True
    
    if state:
        return (img1, img2, position, action), state
    else:
        return (), state
