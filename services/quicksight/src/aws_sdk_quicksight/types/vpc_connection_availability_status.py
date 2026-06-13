"""Generated from Smithy shape ``com.amazonaws.quicksight#VPCConnectionAvailabilityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

VPCConnectionAvailabilityStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
    "PARTIALLY_AVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UNAVAILABLE",
        "PARTIALLY_AVAILABLE",
    )
)


def serialize_json(value: VPCConnectionAvailabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> VPCConnectionAvailabilityStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown VPCConnectionAvailabilityStatus value: {data!r}"
        )
    return cast(VPCConnectionAvailabilityStatus, data)
