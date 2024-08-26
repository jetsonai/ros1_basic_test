# ros1_basic_test

## .bashrc 확인

gedit .bashrc

## Topic Test

<새터미널> 

roscore

<새터미널> 

rosrun ros_basic_test rostopic_pub.py

<새터미널> 

rosrun ros_basic_test rostopic_sub.py

<새터미널> 

rosnode list

rostopic list

rostopic echo /counter

* 모든 창을 닫아주세요

## Customed Message Topic Test

<새터미널>

roscore

<새터미널>

rosrun ros_basic_topicmsg info_publisher.py

<새터미널>

rosrun ros_basic_topicmsg info_subscriber.py

<새터미널>

rosnode list

rostopic list

rostopic echo /counter

rqt_graph

## launch

roslaunch ros_basic_topicmsg ros_topic_test.launch 

* 모든 창을 닫아주세요

## Service Test

<새터미널> 

roscore

<새터미널> 

rosrun ros_basic_service srv_server.py

<새터미널> 

rosrun ros_basic_service srv_client.py Hello my friend

<새터미널> 

rosservice list

rosservice info /word_count

rosservice call /word_count "Hello my friend?"

* 모든 창을 닫아주세요

## Action Service Test (기본)

<새터미널> 

roscore

<새터미널> 

rosrun ros_basic_action simple_action_server.py

<새터미널> 

rosrun ros_basic_action simple_action_client.py

<새터미널> 

rostopic list

* 모든 창을 닫아주세요

## Action Service Test (full)

<새터미널> 

roscore

<새터미널> 

rosrun ros_basic_asynctest async_action_server.py

<새터미널> 

rosrun ros_basic_asynctest async_action_client.py

<새터미널> 

rostopic list

* 모든 창을 닫아주세요

## Camera 테스트

<새터미널> 

roslaunch ros_sensor_test camera_test.launch

카메라 창에서 'q'를 눌러서 종료

터미널에서 Ctl-C

## Lidar 테스트

<새터미널> 

rosrun hls_lfcd_lds_driver view_hlds_laser.launch

## Lidar 테스트

<새터미널> 

rosrun ros_sensor_test lidar_nodeL.py

<손을 가까이 대어 터미널 창의 메시지 로그 확인>

