"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

CapacityReservationPreference: TypeAlias = Literal[
    "RESERVATIONS_ONLY",
    "RESERVATIONS_FIRST",
    "RESERVATIONS_EXCLUDED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESERVATIONS_ONLY",
        "RESERVATIONS_FIRST",
        "RESERVATIONS_EXCLUDED",
    )
)


def serialize_aws_json_1_1(value: CapacityReservationPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityReservationPreference:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityReservationPreference value: {data!r}"
        )
    return cast(CapacityReservationPreference, data)
