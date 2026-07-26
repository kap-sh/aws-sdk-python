"""Generated from Smithy shape ``com.amazonaws.medialive#H265ScanType``."""

from typing import Literal, TypeAlias, cast

"""H265 Scan Type"""
H265ScanType: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265ScanType) -> str:
    return value


def deserialize_json(data: str) -> H265ScanType:
    return cast(H265ScanType, data)
