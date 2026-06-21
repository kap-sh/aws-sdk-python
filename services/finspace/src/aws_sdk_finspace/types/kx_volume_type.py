"""Generated from Smithy shape ``com.amazonaws.finspace#KxVolumeType``."""

from typing import Literal, TypeAlias, cast

KxVolumeType: TypeAlias = Literal["NAS_1",]


# --- restJson1 ser/de ---
def serialize_json(value: KxVolumeType) -> str:
    return value


def deserialize_json(data: str) -> KxVolumeType:
    return cast(KxVolumeType, data)
