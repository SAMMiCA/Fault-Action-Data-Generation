import random
from PIL import Image

actions = ["Crouch", "Stand"]

def get_data_crouch(controller, positions, normal, done_position_action_sets):
    position = random.choice(positions)
    action = random.choice(actions)

    state = False
    if (position, action) not in done_position_action_sets:
        controller.step(
            action="Teleport",
            position=position,
            rotation=dict(x=0, y=random.uniform(0, 360), z=0)
        )
        
        if controller.last_event.metadata['lastActionSuccess'] == True:
            if action == 'Crouch':
                controller.step(action='Stand')
            else:
                controller.step(action='Crouch')
            
            if controller.last_event.metadata['lastActionSuccess'] == True:
                img1 = Image.fromarray(controller.last_event.frame)
                
                if normal:
                    controller.step(action=action)
                
                if controller.last_event.metadata['lastActionSuccess'] == True:
                    img2 = Image.fromarray(controller.last_event.frame)
                    state = True
    
    if state:
        return (img1, img2, position, action), state
    else:
        return (), state
