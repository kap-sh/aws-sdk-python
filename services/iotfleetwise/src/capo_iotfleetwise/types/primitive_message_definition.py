"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#PrimitiveMessageDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.ros2_primitive_message_definition


class _PrimitiveMessageDefinition_ros2PrimitiveMessageDefinition(
    TypedDict, closed=True
):
    ros2PrimitiveMessageDefinition: "capo_iotfleetwise.types.ros2_primitive_message_definition.ROS2PrimitiveMessageDefinition"


PrimitiveMessageDefinition: TypeAlias = (
    _PrimitiveMessageDefinition_ros2PrimitiveMessageDefinition
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrimitiveMessageDefinition) -> dict:
    if "ros2PrimitiveMessageDefinition" in value:
        import capo_iotfleetwise.types.ros2_primitive_message_definition

        return {
            "ros2PrimitiveMessageDefinition": capo_iotfleetwise.types.ros2_primitive_message_definition.serialize_aws_json_1_0(
                value["ros2PrimitiveMessageDefinition"]
            )
        }
    else:
        raise SerializationError("PrimitiveMessageDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> PrimitiveMessageDefinition:
    if "ros2PrimitiveMessageDefinition" in data:
        import capo_iotfleetwise.types.ros2_primitive_message_definition

        return {
            "ros2PrimitiveMessageDefinition": capo_iotfleetwise.types.ros2_primitive_message_definition.deserialize_aws_json_1_0(
                data["ros2PrimitiveMessageDefinition"]
            )
        }
    else:
        raise DeserializationError(
            "PrimitiveMessageDefinition: no recognized variant key"
        )
