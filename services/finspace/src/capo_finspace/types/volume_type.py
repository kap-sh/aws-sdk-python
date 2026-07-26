"""Generated from Smithy shape ``com.amazonaws.finspace#VolumeType``."""

from typing import Literal, TypeAlias, cast

VolumeType: TypeAlias = Literal["NAS_1",]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeType) -> str:
    return value


def deserialize_json(data: str) -> VolumeType:
    return cast(VolumeType, data)
