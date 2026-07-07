"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ROS2PrimitiveMessageDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.double
    import aws_sdk_iotfleetwise.types.max_string_size
    import aws_sdk_iotfleetwise.types.ros2_primitive_type


class ROS2PrimitiveMessageDefinition(TypedDict, closed=True):
    primitive_type: "aws_sdk_iotfleetwise.types.ros2_primitive_type.ROS2PrimitiveType"
    """<p>The primitive type (integer, floating point, boolean, etc.) for the ROS 2 primitive message definition.</p>"""
    offset: NotRequired["aws_sdk_iotfleetwise.types.double.double"]
    """<p>The offset used to calculate the signal value. Combined with scaling, the calculation is <code>value = raw_value * scaling + offset</code>.</p>"""
    scaling: NotRequired["aws_sdk_iotfleetwise.types.double.double"]
    """<p>A multiplier used to decode the message.</p>"""
    upper_bound: NotRequired["aws_sdk_iotfleetwise.types.max_string_size.maxStringSize"]
    """<p>An optional attribute specifying the upper bound for <code>STRING</code> and <code>WSTRING</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ROS2PrimitiveMessageDefinition) -> dict:
    out: dict = {}
    import aws_sdk_iotfleetwise.types.ros2_primitive_type

    out["primitiveType"] = (
        aws_sdk_iotfleetwise.types.ros2_primitive_type.serialize_aws_json_1_0(
            value["primitive_type"]
        )
    )
    if "offset" in value:
        out["offset"] = value["offset"]
    if "scaling" in value:
        out["scaling"] = value["scaling"]
    if "upper_bound" in value:
        out["upperBound"] = value["upper_bound"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ROS2PrimitiveMessageDefinition:
    out: ROS2PrimitiveMessageDefinition = {}  # type: ignore[typeddict-item]
    if "primitiveType" in data:
        import aws_sdk_iotfleetwise.types.ros2_primitive_type

        out["primitive_type"] = (
            aws_sdk_iotfleetwise.types.ros2_primitive_type.deserialize_aws_json_1_0(
                data["primitiveType"]
            )
        )
    else:
        raise DeserializationError(
            "ROS2PrimitiveMessageDefinition.primitive_type required"
        )
    if "offset" in data:
        out["offset"] = data["offset"]
    if "scaling" in data:
        out["scaling"] = data["scaling"]
    if "upperBound" in data:
        out["upper_bound"] = data["upperBound"]
    return out
