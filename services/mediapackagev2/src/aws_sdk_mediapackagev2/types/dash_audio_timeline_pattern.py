"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashAudioTimelinePattern``."""

from typing import Literal, TypeAlias, cast

DashAudioTimelinePattern: TypeAlias = Literal[
    "NONE",
    "PATTERNED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DashAudioTimelinePattern) -> str:
    return value


def deserialize_json(data: str) -> DashAudioTimelinePattern:
    return cast(DashAudioTimelinePattern, data)
