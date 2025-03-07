#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/joint_state.hpp"

class JointStatePublisher : public rclcpp::Node
{

    private:

        rclcpp::Publisher<sensor_msgs::msg::JointState>::SharedPtr joint_state_publisher;
        rclcpp::TimerBase::SharedPtr timer;
        sensor_msgs::msg::JointState joint_state;

        void publish_joint_states()
        {
            joint_state.header.stamp = now();
            joint_state_publisher->publish(joint_state);
        }

    public:
        JointStatePublisher() : Node("joint_state_publisher")
        {
            joint_state_publisher = this->create_publisher<sensor_msgs::msg::JointState>("/joint_states", 10);
            timer = this->create_wall_timer(std::chrono::milliseconds(100), std::bind(&JointStatePublisher::publish_joint_states, this));
            joint_state.name = {"joint_01", "joint_23", "joint_45", "joint_67"};
            joint_state.position = {0.0, 0.0, 0.0, 1.571};
            joint_state.velocity = {0.0, 0.0, 0.0, 0.0};
            joint_state.effort = {0.0, 0.0, 0.0, 0.0};
        }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<JointStatePublisher>());
    rclcpp::shutdown();
    return 0;
}