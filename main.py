from ai2thor.controller import Controller
from arguments import get_args
import time
import os

kitchens = [f"FloorPlan{i}" for i in range(1, 31)]
living_rooms = [f"FloorPlan{200 + i}" for i in range(1, 31)]
bedrooms = [f"FloorPlan{300 + i}" for i in range(1, 31)]
bathrooms = [f"FloorPlan{400 + i}" for i in range(1, 31)]
scenes = kitchens + living_rooms + bedrooms + bathrooms

args = get_args()
if args.target_action == 'movement':
    from action.movement import get_data_movement
elif args.target_action == 'crouch':
    from action.crouch import get_data_crouch
elif args.target_action == 'pickup':
    from action.pickup import get_data_pickup

DATA_ROOT = args.save_root+args.target_action+'/'+args.target_state+'/'

if args.target_state == 'normal':
    normal = True
elif args.target_state == 'fault':
    normal = False

for scene in scenes:
    print("scene", scene)
    if not os.path.isdir(DATA_ROOT+scene):
        os.makedirs(DATA_ROOT+scene)
    
    controller = Controller(
        agentMode="default",
        visibilityDistance=1.5,
        scene=scene,

        # step sizes
        gridSize=0.25,
        snapToGrid=True,
        rotateStepDegrees=90,

        # image modalities
        renderDepthImage=False,
        renderInstanceSegmentation=False,
        renderClassImage=True,

        # camera properties
        width=300,
        height=300,
        fieldOfView=args.fov
    )

    event = controller.step("MoveAhead")

    done_position_action_sets = []

    positions = controller.step(
        action="GetReachablePositions"
    ).metadata["actionReturn"]

    i = 0

    time_start = time.time()
    
    for j in range(args.max_data_num):
        if args.target_action == 'movement':
            data, state = get_data_movement(controller, positions, normal, done_position_action_sets, 
                                args.move_mag, args.rotate_deg, args.move_fault_dist, args.move_fault_dist_rate, args.rotate_fault_deg, args.rotate_fault_deg_rate)
        if args.target_action == 'crouch':
            data, state = get_data_crouch(controller, positions, normal, done_position_action_sets)
        if args.target_action == 'pickup':
            data, state = get_data_pickup(controller, positions, normal, 
                                args.max_pickup_dist, args.fov)
        
        if state:
            if len(data)==4:
                (img1, img2, position, action) = data
                done_position_action_sets.append((position, action))
            elif len(data)==3:
                (img1, img2, action) = data
            img1.save(DATA_ROOT+scene+'/'+str(i)+'_before_'+action+'.jpg')
            img2.save(DATA_ROOT+scene+'/'+str(i)+'_after_'+action+'.jpg')
            i += 1

        time_now = time.time()
        if time_now - time_start > 60*15:
            break
    
    controller.stop()

