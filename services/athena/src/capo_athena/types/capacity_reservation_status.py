"""Generated from Smithy shape ``com.amazonaws.athena#CapacityReservationStatus``."""

from typing import Literal, TypeAlias, cast

CapacityReservationStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "CANCELLING",
    "CANCELLED",
    "FAILED",
    "UPDATE_PENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityReservationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityReservationStatus:
    return cast(CapacityReservationStatus, data)
