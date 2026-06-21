"""Generated from Smithy shape ``com.amazonaws.medialive#CmafKLVBehavior``."""

from typing import Literal, TypeAlias, cast

"""Cmaf KLVBehavior"""
CmafKLVBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafKLVBehavior) -> str:
    return value


def deserialize_json(data: str) -> CmafKLVBehavior:
    return cast(CmafKLVBehavior, data)
