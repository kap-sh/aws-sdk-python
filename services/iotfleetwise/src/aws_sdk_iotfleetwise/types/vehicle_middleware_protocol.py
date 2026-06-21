"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleMiddlewareProtocol``."""

from typing import Literal, TypeAlias, cast

VehicleMiddlewareProtocol: TypeAlias = Literal["ROS_2",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VehicleMiddlewareProtocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VehicleMiddlewareProtocol:
    return cast(VehicleMiddlewareProtocol, data)
