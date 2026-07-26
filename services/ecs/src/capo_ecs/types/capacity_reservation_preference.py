"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

CapacityReservationPreference: TypeAlias = Literal[
    "RESERVATIONS_ONLY",
    "RESERVATIONS_FIRST",
    "RESERVATIONS_EXCLUDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityReservationPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityReservationPreference:
    return cast(CapacityReservationPreference, data)
