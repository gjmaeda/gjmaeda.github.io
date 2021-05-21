# !/usr/bin/env python2
from __future__ import print_function
from __future__ import division


import Movie_Tools


if 0: # generalization in real experiments

    file_name = './Carlos/Human_robot_joint_learning.mp4'

    m = Movie_Tools.Movie_Tools(file_name, start_end = [2, 5], cropXY1 = [0,0], cropXY2 = [150000,150000])
    m.scale_sound(0)
    m.brightness_scale(1.0)
    m.resize_and_speed(2.0, 1.0)
    m.write_as_gif(fps=10)

if 1: # generalization in real experiments

    file_name = './PPMP/small_video_fast.avi'

    m = Movie_Tools.Movie_Tools(file_name, start_end = [0.5, 5.5], cropXY1 = [0,0], cropXY2 = [150000,150000])
    m.scale_sound(0)
    m.brightness_scale(1.0)
    m.resize_and_speed(2.5, 1.0)
    m.write_as_gif(fps=9)



if 0: # generalization in real experiments

    file_name = '../step2_simple_movement_and_eight/real_experiment_simple_movement.avi'

    m = Movie_Tools.Movie_Tools(file_name, start_end = [10, 22], cropXY1 = [0,0], cropXY2 = [150000,150000])
    m.scale_sound(0)
    m.brightness_scale(1.0)
    m.resize_and_speed(2.0, 2.0)
    m.write_as_gif(fps=15, file_name='real_experiment_simple_movement_part2.gif')



if 0: # generalization in real experiments

    file_name = '../step2_simple_movement_and_eight/real_experiment_simple_movement.avi'

    m = Movie_Tools.Movie_Tools(file_name, start_end = [0, 9], cropXY1 = [0,0], cropXY2 = [150000,150000])
    m.scale_sound(0)
    m.brightness_scale(1.0)
    m.resize_and_speed(2.0, 2.0)
    m.write_as_gif(fps=15, file_name='real_experiment_simple_movement_part1.gif')



if 0: # generalization in simulation

    file_name = '../step2_simple_movement_and_eight/simulation_simple_movement.avi'
    duration = 4 # duration of video in seconds
    m = Movie_Tools.Movie_Tools(file_name, start_end = [0, duration], cropXY1 = [0,0], cropXY2 = [150000,150000])
    m.scale_sound(0)
    m.brightness_scale(1.0)
    m.resize_and_speed(2.0, 3.5)
    m.write_as_gif(fps=15, file_name='2019-10-04_generalization_simulation_simple_movement_part1.gif')

if 0:  # generalization in simulation

    print("dddddddd")
    file_name = '../step2_simple_movement_and_eight/simulation_simple_movement.avi'
    m = Movie_Tools.Movie_Tools(file_name, start_end = [6.005, 12.0], cropXY1 = [0,0], cropXY2 = [150000,150000])
    m.scale_sound(0)
    m.brightness_scale(1.0)
    m.resize_and_speed(2.0, 5.05)
    m.write_as_gif(fps=15, file_name='2019-10-04_generalization_simulation_simple_movement_part2.gif')



if 0: # human demo of simple strocke

    file_name = '../step2_simple_movement_and_eight/step2_demonstration_simple_stroke_and_eight.avi'

    duration = 10 # duration of video in seconds
    m = Movie_Tools.Movie_Tools(file_name, start_end = [14, 14+duration], cropXY1 = [0,0], cropXY2 = [150000,150000])
    m.scale_sound(0)
    #m.rotate(angle=90)
    m.brightness_scale(1.0)
    m.resize_and_speed(2.0, 1.25)
    #m.overlay_text('1x', position='bottom', fontsize=40, duration=duration//m.speed_factor)
    #m.write_as_video(fps=20)

    m.write_as_gif(fps=10, file_name='2019-10-04_human_demo_eight_shape.gif')

if 0:  # human demo of simple strocke

    file_name = '../step2_simple_movement_and_eight/step2_demonstration_simple_stroke_and_eight.avi'

    duration = 9  # duration of video in seconds
    m = Movie_Tools.Movie_Tools(file_name, start_end=[0, duration], cropXY1=[0, 0], cropXY2=[150000, 150000])
    m.scale_sound(0)
    # m.rotate(angle=90)
    m.brightness_scale(1.0)
    m.resize_and_speed(2.0, 1.25)
    # m.overlay_text('1x', position='bottom', fontsize=40, duration=duration//m.speed_factor)
    # m.write_as_video(fps=20)

    m.write_as_gif(fps=10, file_name='2019-10-04_simple_stroke.gif')


















