"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CustomAdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

CustomAdType: TypeAlias = Literal[
    "PROGRAM",
    "CHAPTER",
    "UNSCHEDULED_EVENT",
    "ALTERNATE_CONTENT_OPPORTUNITY",
    "NETWORK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROGRAM",
        "CHAPTER",
        "UNSCHEDULED_EVENT",
        "ALTERNATE_CONTENT_OPPORTUNITY",
        "NETWORK",
    )
)


def serialize_json(value: CustomAdType) -> str:
    return value


def deserialize_json(data: str) -> CustomAdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomAdType value: {data!r}")
    return cast(CustomAdType, data)
