"""Generated from Smithy shape ``com.amazonaws.sagemaker#AICapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AICapacityReservationPreference: TypeAlias = Literal["capacity-reservations-only",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("capacity-reservations-only",))


def serialize_aws_json_1_1(value: AICapacityReservationPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AICapacityReservationPreference:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AICapacityReservationPreference value: {data!r}"
        )
    return cast(AICapacityReservationPreference, data)
