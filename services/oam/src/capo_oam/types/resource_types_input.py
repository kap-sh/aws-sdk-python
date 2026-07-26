"""Generated from Smithy shape ``com.amazonaws.oam#ResourceTypesInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_oam.types.resource_type

ResourceTypesInput: TypeAlias = list["capo_oam.types.resource_type.ResourceType"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypesInput) -> list:
    import capo_oam.types.resource_type

    out: list = []
    for item in value:
        out.append(capo_oam.types.resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTypesInput:
    import capo_oam.types.resource_type

    out: ResourceTypesInput = []
    for item in data:
        out.append(capo_oam.types.resource_type.deserialize_json(item))
    return out
