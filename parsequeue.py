from mocap import Trial
from mocap import Subject
import json
import math

animations = [
    [18, 1, 0.5],
    [18, 2, 0.5],
    [18, 3, -0.5],
    [18, 4, -0.5],
    [18, 5, -0.5],
    [18, 6, -0.5],
    [18, 7, -0.1],
    [18, 8, 0.2],
    [18, 9, 0.3],
    [18, 10, -0.7],
    [18, 11, -0.7],
    [18, 12, 0.5],
    [18, 13, -0.7],
    [18, 14, -0.7],
    [18, 15, 0.7],
    [19, 1, 0.5],
    [19, 2, 0.5],
    [19, 3, -0.5],
    [19, 4, -0.5],
    [19, 5, -0.5],
    [19, 6, -0.5],
    [19, 7, -0.1],
    [19, 8, 0.2],
    [19, 9, 0.3],
    [19, 10, -0.7],
    [19, 11, -0.7],
    [19, 12, 0.5],
    [19, 13, -0.7],
    [19, 14, -0.7],
    [19, 15, 0.7],
    [2, 6, 0.8],
    [2, 10, 0.9],
    [13, 1, 0.6],
    [13, 2, 0.6],
    [13, 3, 0.6],
    [13, 4, 0.5],
    [13, 5, -0.8],
    [13, 6, -0.8],
    [13, 7, 1],
    [13, 8, 0.9],
    [13, 9, 1],
    [13, 10, -0.1],
    [13, 12, -0.1],
    [13, 14, 1],
    [13, 15, 1],
    [13, 16, 1],
    [13, 20, 0.1],
    [13, 21, 0.1],
    [13, 22, 0.1],
    [13, 23, -0.1],
    [13, 24, -0.1],
    [13, 25, -0.1],
    [13, 33, -0.3],
    [13, 34, -0.3],
    [13, 35, 0.5],
    [13, 36, 0.5],
    [13, 37, 0.5],
    [13, 38, 0.5],
    [14, 4, 0.9],
    [14, 5, 0.9],
    [14, 7, -0.3],
    [14, 8, -0.3],
    [14, 9, -0.3],
    [14, 10, -0.1],
    [14, 11, -0.1],
    [14, 12, -0.1],
    [14, 13, 0],
    [14, 15, 0],
    [14, 16, -0.3],
    [14, 17, 1],
    [14, 18, 1],
    [14, 19, 1],
    [14, 21, 0.5],
    [14, 22, 0.5],
    [14, 23, 0.5],
    [14, 27, 0.6],
    [14, 28, 0.6],
    [14, 29, 0.7],
    [14, 30, 0.5],
    [14, 31, 0.5],
    [14, 32, 0.5],
    [14, 33, -0.3],
    [14, 34, -0.3],
    [14, 35, -0.3],
    [14, 36, 0.5],
    [14, 37, 0.9],
    [15, 2, 0.3],
    [15, 6, -0.1],
    [15, 7, -0.1],
    [15, 10, 0.4],
    [26, 9, 0.3],
    [26, 10, 0.7],
    [26, 11, 0.7],
    [40, 6, -0.7],
    [40, 7, -0.3],
    [40, 8, -0.3],
    [40, 9, -0.3],
    [40, 10, 0],
    [40, 11, 0],
    [41, 7, -0.4],
    [41, 8, -0.4],
    [41, 9, -0.4],
    [20, 1, 0.7],
    [20, 2, 0.2],
    [20, 3, 0.2],
    [20, 4, 0],
    [20, 5, 0],
    [20, 6, 0],
    [20, 7, 0],
    [20, 8, -0.1],
    [20, 9, 1],
    [20, 10, 0.35],
    [20, 11, 0.8],
    [20, 12, 0.8],
    [20, 13, -0.1],
    [21, 1, 0.7],
    [21, 2, 0.2],
    [21, 3, 0.2],
    [21, 4, 0],
    [21, 5, 0],
    [21, 6, 0],
    [21, 7, 0],
    [21, 8, -0.1],
    [21, 9, 1],
    [21, 10, 0.35],
    [21, 11, 0.8],
    [21, 12, 0.8],
    [21, 13, -0.1],
    [23, 1, 0],
    [23, 2, 0],
    [23, 3, 1],
    [23, 4, 1],
    [23, 5, 0],
    [23, 6, 1],
    [23, 7, 0],
    [23, 8, 0.5],
    [23, 9, 0.5],
    [23, 10, 0],
    [23, 11, 1],
    [23, 12, 0],
    [23, 13, 0.1],
    [23, 14, 0.3],
    [23, 15, 0.5],
    [23, 16, 0.5],
    [23, 17, -0.2],
    [23, 18, 0],
    [23, 19, -0.3],
    [23, 20, -0.5],
    [23, 21, -0.6],
    [23, 22, 0.3],
    [22, 1, 0],
    [22, 2, 0],
    [22, 20, -1]
]


def rad_to_deg(rads):
    return (rads * 180) / math.pi


def to_json(subject, trial):
    json_array = []

    motions = trial.get_motions()
    joints = subject.get_joints()
    for i in range(len(motions)):
        json = {}
        json['state'] = trial.get_sentiment()

        joints['root'].set_motion(motions[i])
        dict = joints['root'].to_dict()
        lhand = dict['lhand']
        rhand = dict['rhand']
        l_coords = lhand.coordinate
        l_rotation = lhand.rotation
        r_coords = rhand.coordinate
        r_rotation = rhand.rotation

        json['leftHandPositionX'] = l_coords[0][0]
        json['leftHandPositionY'] = l_coords[1][0]
        json['leftHandPositionZ'] = l_coords[2][0]
        json['leftHandRotationX'] = rad_to_deg(l_rotation[0])
        json['leftHandRotationY'] = rad_to_deg(l_rotation[1])
        json['leftHandRotationZ'] = rad_to_deg(l_rotation[2])
        json['rightHandPositionX'] = r_coords[0][0]
        json['rightHandPositionY'] = r_coords[1][0]
        json['rightHandPositionZ'] = r_coords[2][0]
        json['rightHandRotationX'] = rad_to_deg(r_rotation[0])
        json['rightHandRotationY'] = rad_to_deg(r_rotation[1])
        json['rightHandRotationZ'] = rad_to_deg(r_rotation[2])

        json_array.append(json)

    return json_array


print("Animation Parser")
i = 0
for animation in animations:
    print("Starting animation {}:".format(i))
    subject = Subject(str(animation[0]).zfill(2))
    trial = Trial(str(animation[1]).zfill(2), subject, animation[2])
    print("Parsing...")
    arr = to_json(subject, trial)
    print("Saving...")
    with open('./json/{}.json'.format(i), 'w') as outfile:
        json.dump(arr, outfile)
    print("Done!")
    i = i + 1

print("Finished all animations in queue")
