import random
from PIL import Image
import math

objects = ['Book', 'Bowl', 'CellPhone', 'CreditCard', 'Mug', 'TissueBox', 'Vase']

OBJ_COLOR = {'HousePlant': (73, 144, 213), 'DeskLamp': (99, 164, 25), 'GarbageBag': (250, 186, 207), 'PepperShaker': (5, 204, 214), 'Cloth': (110, 184, 56), 'Window': (200, 150, 134), 'SinkBasin': (80, 192, 81), 'ShowerDoor': (36, 253, 61), 'Plate': (188, 154, 128), 'ShowerHead': (248, 167, 29), 'Apple': (159, 98, 144), 'Footstool': (74, 187, 51), 'TowelHolder': (232, 28, 225), 'ShowerCurtain': (60, 12, 39), 'Cup': (35, 71, 130), 'ScrubBrush': (222, 148, 80), 'Newspaper': (19, 196, 2), 'Kettle': (7, 83, 48), 'WateringCan': (147, 67, 249), 'Vase': (83, 152, 69), 'BaseballBat': (171, 20, 38), 'Chair': (166, 13, 176), 'TennisRacket': (138, 71, 107), 'VacuumCleaner': (230, 13, 166), 'CounterTop': (103, 209, 30), 'Cabinet': (210, 149, 89), 'Pen': (239, 130, 152), 'Pillow': (217, 193, 130), 'ShowerGlass': (80, 68, 237), 'Laptop': (20, 107, 222), 'SprayBottle': (89, 126, 121), 'Watch': (242, 6, 88), 'Potato': (187, 142, 9), 'Bread': (18, 150, 252), 'Towel': (170, 186, 210), 'Spatula': (30, 98, 242), 'Mug': (8, 94, 186), 'ArmChair': (96, 52, 68), 'HandTowel': (182, 187, 236), 'Safe': (198, 238, 160), 'Poster': (145, 87, 153), 'Pot': (132, 237, 87), 'Candle': (233, 102, 178), 'Ladle': (174, 98, 216), 'Blinds': (214, 223, 197), 'Pencil': (177, 226, 23), 'Fork': (54, 200, 25), 'AlarmClock': (184, 20, 170), 'TVStand': (94, 234, 136), 'CoffeeTable': (18, 14, 75), 'BasketBall': (97, 58, 36), 'CreditCard': (56, 235, 12), 'TeddyBear': (229, 73, 134), 'HandTowelHolder': (58, 218, 247), 'StoveKnob': (106, 252, 95), 'Ottoman': (160, 135, 174), 'Plunger': (74, 209, 56), 'WineBottle': (53, 130, 252), 'Dresser': (51, 128, 146), 'Toilet': (21, 27, 163), 'Desk': (14, 120, 179), 'DiningTable': (83, 33, 33), 'Bottle': (64, 80, 115), 'Dumbbell': (45, 57, 144), 'SaltShaker': (36, 222, 26), 'Tomato': (119, 189, 121), 'KeyChain': (27, 54, 18), 'StoveBurner': (156, 249, 101), 'RoomDecor': (216, 96, 246), 'GarbageCan': (225, 40, 55), 'Drawer': (155, 30, 210), 'Book': (43, 31, 148), 'ShelvingUnit': (125, 226, 119), 'Bowl': (209, 182, 193), 'Pan': (246, 212, 161), 'DogBed': (106, 193, 45), 'Television': (27, 245, 217), 'ToiletPaperHanger': (124, 32, 10), 'Faucet': (21, 38, 98), 'LaundryHamper': (35, 109, 26), 'LightSwitch': (11, 51, 121), 'SoapBottle': (168, 222, 137), 'Curtains': (6, 62, 102), 'BathtubBasin': (109, 206, 121), 'Desktop': (35, 16, 64), 'AluminumFoil': (181, 163, 89), 'CoffeeMachine': (147, 71, 238), 'Floor': (243, 246, 208), 'Stool': (13, 54, 156), 'RemoteControl': (187, 19, 208), 'Sofa': (82, 143, 39), 'Toaster': (55, 33, 114), 'SoapBar': (43, 97, 155), 'TableTopDecor': (126, 204, 158), 'CD': (65, 112, 172), 'ButterKnife': (135, 147, 55), 'PaperTowelRoll': (144, 173, 28), 'Bathtub': (59, 170, 176), 'Statue': (243, 75, 41), 'Boots': (121, 126, 101), 'Spoon': (235, 57, 90), 'Microwave': (54, 96, 202), 'Mirror': (36, 3, 222), 'Fridge': (91, 156, 207), 'SideTable': (202, 45, 114), 'Sink': (30, 181, 88), 'DishSponge': (166, 58, 136), 'Egg': (240, 75, 163), 'Box': (60, 252, 230), 'Shelf': (39, 54, 158), 'Knife': (211, 157, 122), 'ToiletPaper': (162, 204, 152), 'CellPhone': (227, 98, 136), 'TissueBox': (98, 43, 249), 'FloorLamp': (253, 73, 35), 'Painting': (40, 117, 236), 'Lettuce': (203, 156, 88), 'Bed': (209, 156, 101)}

def dist(a, b, xz=False):
    a_x, a_y, a_z = a['x'], a['y'], a['z']
    b_x, b_y, b_z = b['x'], b['y'], b['z']
    
    if not xz:
        return math.sqrt((a_x-b_x)**2+(a_y-b_y)**2+(a_z-b_z)**2)
    else:
        return math.sqrt((a_x-b_x)**2+(a_z-b_z)**2)

def object_xyz(o):
    bounds = o['axisAlignedBoundingBox']['cornerPoints']
    min_x, min_z = bounds[0][0], bounds[0][2]
    max_x, max_y, max_z = bounds[0]
    
    for (x,y,z) in bounds[1:]:
        if x<min_x: min_x=x
        if z<min_z: min_z=z
        if x>max_x: max_x=x
        if z>max_z: max_z=y
    
    return ((min_x, max_x), max_y, (min_z, max_z))

def sort_object_xyz(os):
    xyzs = [(object_xyz(o), o['objectType']) for o in os if o['objectType']!='Floor']
    ys = [-w[1] for w, o in xyzs]
    
    _, xyzs = (list(t) for t in zip(*sorted(zip(ys, xyzs))))
    return xyzs

def get_position(xyzs, o, bounds):
    size = o['axisAlignedBoundingBox']['size']
    max_size = max(size['x'], size['y'], size['z']) + 0.03
    
    check = False

    while True:
        x, z = random.uniform(*bounds['x']), random.uniform(*bounds['z'])
        
        for xyz, oo in xyzs:
            (min_x, max_x), max_y, (min_z, max_z) = xyz
            if x > min_x and x < max_x and z > min_z and z < max_z:
                y = max_y + max_size
                check = True
                break
        
        if check:
            break
    
    position_place = ({'x':x, 'y':y, 'z':z}, oo)
    return position_place

def get_data_pickup(controller, positions, normal, MAX_PICKUP_DIST=1.0, FOV=90):
    b = controller.last_event.metadata['sceneBounds']
    bounds = {'x':(b['center']['x'] - b['size']['x']/2, b['center']['x'] + b['size']['x']/2), 
              'y':(b['center']['y'] - b['size']['y']/2, b['center']['y'] + b['size']['y']/2), 
              'z':(b['center']['z'] - b['size']['z']/2, b['center']['z'] + b['size']['z']/2)}

    xyzs = sort_object_xyz(controller.last_event.metadata['objects'])

    exists = [m['objectType'] for m in controller.last_event.metadata['objects'] if m['objectType'] in objects]
    obj = random.choice(exists)

    action = 'Pickup'
    for m in controller.last_event.metadata['objects']:
        state = False
        if m['objectType'] == obj:
            obj_id = m['objectId']

            position_count = 0
            reset_count = 0
            reset = False
            
            c = m['axisAlignedBoundingBox']['center']
            able_positions = [p for p in positions if dist(c,p,xz=True)<=MAX_PICKUP_DIST]
            
            if len(able_positions)>0:
                for i in range(100):
                    position = random.choice(able_positions)

                    controller.step(
                        action="Teleport",
                        position=position,
                        rotation=dict(x=0, y=random.uniform(0, FOV), z=0)
                    )

                    if controller.last_event.metadata['lastActionSuccess'] == True:
                        state = True
                        break
            if state:
                state2 = False
                for k in range(math.ceil(360/FOV)):
                    segs = []
                    
                    controller.step(
                        action="LookUp",
                        degrees=30
                    )
                    segs.append(controller.last_event.class_segmentation_frame)

                    controller.step(
                        action="LookDown",
                        degrees=30
                    )
                    segs.append(controller.last_event.class_segmentation_frame)

                    controller.step(
                        action="LookDown",
                        degrees=30
                    )
                    segs.append(controller.last_event.class_segmentation_frame)

                    controller.step(
                        action="LookUp",
                        degrees=30
                    )
                    
                    pixel_counts = [(s == OBJ_COLOR[obj]).sum() for s in segs]
                    max_count = -1
                    idx_counts = []
                    for p in range(len(pixel_counts)):
                        if pixel_counts[p] > max_count:
                            idx_counts = [p]
                            max_count = pixel_counts[p]
                        elif pixel_counts[p] == max_count:
                            idx_counts.append(p)
                    max_idx = random.choice(idx_counts)
                    
                    if max_idx == 0:
                        controller.step(
                            action="LookUp",
                            degrees=30
                        )
                    elif max_idx == 2:
                        controller.step(
                            action="LookDown",
                            degrees=30
                        )

                    img1 = Image.fromarray(controller.last_event.frame)

                    if normal:
                        controller.step(
                            action="PickupObject",
                            objectId=obj_id,
                            forceAction=False,
                            manualInteract=False
                        )

                    if controller.last_event.metadata['lastActionSuccess'] == True:
                        img2 = Image.fromarray(controller.last_event.frame)

                        if max_idx == 0:
                            controller.step(
                                action="LookDown",
                                degrees=30
                            )
                        elif max_idx == 2:
                            controller.step(
                                action="LookUp",
                                degrees=30
                            )
                        state2 = True
                        
                        break;
                    else:
                        if max_idx == 0:
                            controller.step(
                                action="LookDown",
                                degrees=30
                            )
                        elif max_idx == 2:
                            controller.step(
                                action="LookUp",
                                degrees=30
                            )
            
            while True:
                position_place, target = get_position(xyzs, m, bounds)

                controller.step(
                    action="PlaceObjectAtPoint",
                    objectId=obj_id,
                    position=position_place
                )
                
                if controller.last_event.metadata['lastActionSuccess'] == True:
                    break;
        
        if state and state2:
            break

    if not state:
        return (), state
    elif not state2:
        return (), state2
    else:
        return (img1, img2, action+'_'+obj), state2

