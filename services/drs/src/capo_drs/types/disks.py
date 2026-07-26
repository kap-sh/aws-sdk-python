"""Generated from Smithy shape ``com.amazonaws.drs#Disks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.disk

Disks: TypeAlias = list["capo_drs.types.disk.Disk"]


# --- restJson1 ser/de ---
def serialize_json(value: Disks) -> list:
    import capo_drs.types.disk

    out: list = []
    for item in value:
        out.append(capo_drs.types.disk.serialize_json(item))
    return out


def deserialize_json(data: list) -> Disks:
    import capo_drs.types.disk

    out: Disks = []
    for item in data:
        out.append(capo_drs.types.disk.deserialize_json(item))
    return out
