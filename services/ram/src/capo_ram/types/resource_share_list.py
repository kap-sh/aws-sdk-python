"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.resource_share

ResourceShareList: TypeAlias = list["capo_ram.types.resource_share.ResourceShare"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareList) -> list:
    import capo_ram.types.resource_share

    out: list = []
    for item in value:
        out.append(capo_ram.types.resource_share.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceShareList:
    import capo_ram.types.resource_share

    out: ResourceShareList = []
    for item in data:
        out.append(capo_ram.types.resource_share.deserialize_json(item))
    return out
