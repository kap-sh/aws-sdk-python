"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

HarvestJobStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "CANCELLED",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "IN_PROGRESS",
        "CANCELLED",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: HarvestJobStatus) -> str:
    return value


def deserialize_json(data: str) -> HarvestJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarvestJobStatus value: {data!r}")
    return cast(HarvestJobStatus, data)
