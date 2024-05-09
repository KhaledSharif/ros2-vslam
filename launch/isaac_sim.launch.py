import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    """Launch file which brings up visual slam node configured for Isaac Sim."""
    visual_slam_node = ComposableNode(
        name="visual_slam_node",
        plugin="nvidia::isaac_ros::visual_slam::VisualSlamNode",
        remappings=[
            ("stereo_camera/left/image", "front_stereo_camera/left_rgb/image_raw"),
            (
                "stereo_camera/left/camera_info",
                "front_stereo_camera/left_rgb/camerainfo",
            ),
            ("stereo_camera/right/image", "front_stereo_camera/right_rgb/image_raw"),
            (
                "stereo_camera/right/camera_info",
                "front_stereo_camera/right_rgb/camerainfo",
            ),
        ],
        parameters=[
            {
                "use_sim_time": True,
                "denoise_input_images": True,
                "rectified_images": True,
                "enable_slam_visualization": True,
                "enable_observations_view": True,
                "enable_landmarks_view": True,
                "enable_debug_mode": False,
                "debug_dump_path": "/tmp/cuvslam",
                "map_frame": "map",
                "odom_frame": "odom",
                "base_frame": "base_link",
                "input_base_frame": "base_link",
            }
        ],
    )

    visual_slam_launch_container = ComposableNodeContainer(
        name="visual_slam_launch_container",
        namespace="",
        package="rclcpp_components",
        executable="component_container",
        composable_node_descriptions=[
            visual_slam_node,
        ],
        output="screen",
    )

    return launch.LaunchDescription([visual_slam_launch_container])