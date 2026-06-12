"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleMiddlewareProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

VehicleMiddlewareProtocol: TypeAlias = Literal["ROS_2",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("ROS_2",))


def serialize_aws_json_1_0(value: VehicleMiddlewareProtocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VehicleMiddlewareProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VehicleMiddlewareProtocol value: {data!r}")
    return cast(VehicleMiddlewareProtocol, data)
