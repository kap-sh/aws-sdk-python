"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashAudioTimelinePattern``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DashAudioTimelinePattern: TypeAlias = Literal[
    "NONE",
    "PATTERNED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PATTERNED",
    )
)


def serialize_json(value: DashAudioTimelinePattern) -> str:
    return value


def deserialize_json(data: str) -> DashAudioTimelinePattern:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashAudioTimelinePattern value: {data!r}")
    return cast(DashAudioTimelinePattern, data)
