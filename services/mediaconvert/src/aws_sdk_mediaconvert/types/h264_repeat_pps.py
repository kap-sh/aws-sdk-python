"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264RepeatPps``."""

from typing import Literal, TypeAlias, cast

"""Places a PPS header on each encoded picture, even if repeated."""
H264RepeatPps: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264RepeatPps) -> str:
    return value


def deserialize_json(data: str) -> H264RepeatPps:
    return cast(H264RepeatPps, data)
