"""Generated from Smithy shape ``com.amazonaws.connect#TrafficDistributionGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

TrafficDistributionGroupStatus: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "ACTIVE",
    "CREATION_FAILED",
    "PENDING_DELETION",
    "DELETION_FAILED",
    "UPDATE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATION_IN_PROGRESS",
        "ACTIVE",
        "CREATION_FAILED",
        "PENDING_DELETION",
        "DELETION_FAILED",
        "UPDATE_IN_PROGRESS",
    )
)


def serialize_json(value: TrafficDistributionGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> TrafficDistributionGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TrafficDistributionGroupStatus value: {data!r}"
        )
    return cast(TrafficDistributionGroupStatus, data)
