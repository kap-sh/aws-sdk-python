"""Generated from Smithy shape ``com.amazonaws.medialive#H264ScanType``."""

from typing import Literal, TypeAlias, cast

"""H264 Scan Type"""
H264ScanType: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264ScanType) -> str:
    return value


def deserialize_json(data: str) -> H264ScanType:
    return cast(H264ScanType, data)
