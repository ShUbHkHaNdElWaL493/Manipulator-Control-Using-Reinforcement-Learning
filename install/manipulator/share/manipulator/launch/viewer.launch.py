#   CS22B1090
#   Shubh Khandelwal

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    package_dir = get_package_share_directory('manipulator')

    urdf_path = os.path.join(package_dir, 'urdf', 'manipulator.urdf')
    rviz_config_path = os.path.join(package_dir, 'rviz', 'manipulator_config.rviz')

    static_transform_publisher_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        arguments=[
            '--x', '0', '--y', '0', '--z', '0',
            '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1',
            '--frame-id', 'map',
            '--child-frame-id', 'link_0'
        ]
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(urdf_path, 'r').read()}]
    )

    joint_state_publisher_node = Node(
        package='manipulator',
        executable='joint_state_publisher',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config_path],
        output='screen'
    )

    return LaunchDescription([
        static_transform_publisher_node,
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz_node
    ])