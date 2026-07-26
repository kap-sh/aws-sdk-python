"""Generated from Smithy shape ``com.amazonaws.batch#Volumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.volume

Volumes: TypeAlias = list["capo_batch.types.volume.Volume"]


# --- restJson1 ser/de ---
def serialize_json(value: Volumes) -> list:
    import capo_batch.types.volume

    out: list = []
    for item in value:
        out.append(capo_batch.types.volume.serialize_json(item))
    return out


def deserialize_json(data: list) -> Volumes:
    import capo_batch.types.volume

    out: Volumes = []
    for item in data:
        out.append(capo_batch.types.volume.deserialize_json(item))
    return out
