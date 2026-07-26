"""Generated from Smithy shape ``com.amazonaws.synthetics#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.resource_to_tag

ResourceList: TypeAlias = list["capo_synthetics.types.resource_to_tag.ResourceToTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceList) -> list:
    import capo_synthetics.types.resource_to_tag

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.resource_to_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceList:
    import capo_synthetics.types.resource_to_tag

    out: ResourceList = []
    for item in data:
        out.append(capo_synthetics.types.resource_to_tag.deserialize_json(item))
    return out
