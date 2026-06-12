"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

VehicleState: TypeAlias = Literal[
    "CREATED",
    "READY",
    "HEALTHY",
    "SUSPENDED",
    "DELETING",
    "READY_FOR_CHECKIN",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "READY",
        "HEALTHY",
        "SUSPENDED",
        "DELETING",
        "READY_FOR_CHECKIN",
    )
)


def serialize_aws_json_1_0(value: VehicleState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VehicleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VehicleState value: {data!r}")
    return cast(VehicleState, data)
