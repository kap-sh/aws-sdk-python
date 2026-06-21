"""Generated from Smithy shape ``com.amazonaws.sagemaker#AICapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

AICapacityReservationPreference: TypeAlias = Literal["capacity-reservations-only",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AICapacityReservationPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AICapacityReservationPreference:
    return cast(AICapacityReservationPreference, data)
