"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsDataPtsControl``."""

from typing import Literal, TypeAlias, cast

"""If you select ALIGN_TO_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value to allow all PTS values."""
M2tsDataPtsControl: TypeAlias = Literal[
    "AUTO",
    "ALIGN_TO_VIDEO",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsDataPtsControl) -> str:
    return value


def deserialize_json(data: str) -> M2tsDataPtsControl:
    return cast(M2tsDataPtsControl, data)
