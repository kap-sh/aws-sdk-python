"""Generated from Smithy shape ``com.amazonaws.guardduty#Volumes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.volume

Volumes: TypeAlias = list["capo_guardduty.types.volume.Volume"]


# --- restJson1 ser/de ---
def serialize_json(value: Volumes) -> list:
    import capo_guardduty.types.volume

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.volume.serialize_json(item))
    return out


def deserialize_json(data: list) -> Volumes:
    import capo_guardduty.types.volume

    out: Volumes = []
    for item in data:
        out.append(capo_guardduty.types.volume.deserialize_json(item))
    return out
