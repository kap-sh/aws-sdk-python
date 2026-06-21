"""Generated from Smithy shape ``com.amazonaws.sagemaker#CapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

CapacityReservationPreference: TypeAlias = Literal["capacity-reservations-only",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityReservationPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityReservationPreference:
    return cast(CapacityReservationPreference, data)
