"""Generated from Smithy shape ``com.amazonaws.finspace#Volumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.volume

Volumes: TypeAlias = list["aws_sdk_finspace.types.volume.Volume"]


# --- restJson1 ser/de ---
def serialize_json(value: Volumes) -> list:
    import aws_sdk_finspace.types.volume

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.volume.serialize_json(item))
    return out


def deserialize_json(data: list) -> Volumes:
    import aws_sdk_finspace.types.volume

    out: Volumes = []
    for item in data:
        out.append(aws_sdk_finspace.types.volume.deserialize_json(item))
    return out
