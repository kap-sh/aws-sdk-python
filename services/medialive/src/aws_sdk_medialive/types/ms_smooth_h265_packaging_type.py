"""Generated from Smithy shape ``com.amazonaws.medialive#MsSmoothH265PackagingType``."""

from typing import Literal, TypeAlias, cast

"""Ms Smooth H265 Packaging Type"""
MsSmoothH265PackagingType: TypeAlias = Literal[
    "HEV1",
    "HVC1",
]


# --- restJson1 ser/de ---
def serialize_json(value: MsSmoothH265PackagingType) -> str:
    return value


def deserialize_json(data: str) -> MsSmoothH265PackagingType:
    return cast(MsSmoothH265PackagingType, data)
