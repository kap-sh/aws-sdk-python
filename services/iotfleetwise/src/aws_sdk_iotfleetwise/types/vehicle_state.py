"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleState``."""

from typing import Literal, TypeAlias, cast

VehicleState: TypeAlias = Literal[
    "CREATED",
    "READY",
    "HEALTHY",
    "SUSPENDED",
    "DELETING",
    "READY_FOR_CHECKIN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VehicleState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VehicleState:
    return cast(VehicleState, data)
