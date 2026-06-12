"""Generated from Smithy shape ``com.amazonaws.finspace#KxVolumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_volume

KxVolumes: TypeAlias = list["aws_sdk_finspace.types.kx_volume.KxVolume"]


# --- restJson1 ser/de ---
def serialize_json(value: KxVolumes) -> list:
    import aws_sdk_finspace.types.kx_volume

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.kx_volume.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxVolumes:
    import aws_sdk_finspace.types.kx_volume

    out: KxVolumes = []
    for item in data:
        out.append(aws_sdk_finspace.types.kx_volume.deserialize_json(item))
    return out
