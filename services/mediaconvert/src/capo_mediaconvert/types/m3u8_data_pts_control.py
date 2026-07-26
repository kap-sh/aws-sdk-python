"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M3u8DataPtsControl``."""

from typing import Literal, TypeAlias, cast

"""If you select ALIGN_TO_VIDEO, MediaConvert writes captions and data packets with Presentation Timestamp (PTS) values greater than or equal to the first video packet PTS (MediaConvert drops captions and data packets with lesser PTS values). Keep the default value AUTO to allow all PTS values."""
M3u8DataPtsControl: TypeAlias = Literal[
    "AUTO",
    "ALIGN_TO_VIDEO",
]


# --- restJson1 ser/de ---
def serialize_json(value: M3u8DataPtsControl) -> str:
    return value


def deserialize_json(data: str) -> M3u8DataPtsControl:
    return cast(M3u8DataPtsControl, data)
