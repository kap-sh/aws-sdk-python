"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitlingType``."""

from typing import Literal, TypeAlias, cast

"""Specify whether your DVB subtitles are standard or for hearing impaired. Choose hearing impaired if your subtitles include audio descriptions and dialogue. Choose standard if your subtitles include only dialogue."""
DvbSubtitlingType: TypeAlias = Literal[
    "HEARING_IMPAIRED",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubtitlingType) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitlingType:
    return cast(DvbSubtitlingType, data)
