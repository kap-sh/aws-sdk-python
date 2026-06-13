"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CapacityReservationPreferenceEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

CapacityReservationPreferenceEnum: TypeAlias = Literal[
    "capacity-reservations-only",
    "open",
    "none",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "capacity-reservations-only",
        "open",
        "none",
    )
)


def serialize_aws_json_1_0(value: CapacityReservationPreferenceEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CapacityReservationPreferenceEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityReservationPreferenceEnum value: {data!r}"
        )
    return cast(CapacityReservationPreferenceEnum, data)
