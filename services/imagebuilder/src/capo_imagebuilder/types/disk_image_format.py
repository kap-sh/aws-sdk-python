"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DiskImageFormat``."""

from typing import Literal, TypeAlias, cast

DiskImageFormat: TypeAlias = Literal[
    "VMDK",
    "RAW",
    "VHD",
]


# --- restJson1 ser/de ---
def serialize_json(value: DiskImageFormat) -> str:
    return value


def deserialize_json(data: str) -> DiskImageFormat:
    return cast(DiskImageFormat, data)
