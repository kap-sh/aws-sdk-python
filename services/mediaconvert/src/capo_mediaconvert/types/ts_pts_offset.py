"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TsPtsOffset``."""

from typing import Literal, TypeAlias, cast

"""Specify the initial presentation timestamp (PTS) offset for your transport stream output. To let MediaConvert automatically determine the initial PTS offset: Keep the default value, Auto. We recommend that you choose Auto for the widest player compatibility. The initial PTS will be at least two seconds and vary depending on your output's bitrate, HRD buffer size and HRD buffer initial fill percentage. To manually specify an initial PTS offset: Choose Seconds or Milliseconds. Then specify the number of seconds or milliseconds with PTS offset."""
TsPtsOffset: TypeAlias = Literal[
    "AUTO",
    "SECONDS",
    "MILLISECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: TsPtsOffset) -> str:
    return value


def deserialize_json(data: str) -> TsPtsOffset:
    return cast(TsPtsOffset, data)
