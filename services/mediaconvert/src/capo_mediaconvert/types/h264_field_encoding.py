"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264FieldEncoding``."""

from typing import Literal, TypeAlias, cast

"""The video encoding method for your MPEG-4 AVC output. Keep the default value, PAFF, to have MediaConvert use PAFF encoding for interlaced outputs. Choose Force field to disable PAFF encoding and create separate interlaced fields. Choose MBAFF to disable PAFF and have MediaConvert use MBAFF encoding for interlaced outputs."""
H264FieldEncoding: TypeAlias = Literal[
    "PAFF",
    "FORCE_FIELD",
    "MBAFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264FieldEncoding) -> str:
    return value


def deserialize_json(data: str) -> H264FieldEncoding:
    return cast(H264FieldEncoding, data)
