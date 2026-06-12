"""Generated from Smithy shape ``com.amazonaws.securityhub#RegionAvailabilityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

RegionAvailabilityStatus: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UNAVAILABLE",
    )
)


def serialize_json(value: RegionAvailabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> RegionAvailabilityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegionAvailabilityStatus value: {data!r}")
    return cast(RegionAvailabilityStatus, data)
