"""Generated from Smithy shape ``com.amazonaws.datazone#EntityOwners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.owner_properties_output

EntityOwners: TypeAlias = list[
    "capo_datazone.types.owner_properties_output.OwnerPropertiesOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntityOwners) -> list:
    import capo_datazone.types.owner_properties_output

    out: list = []
    for item in value:
        out.append(capo_datazone.types.owner_properties_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> EntityOwners:
    import capo_datazone.types.owner_properties_output

    out: EntityOwners = []
    for item in data:
        out.append(capo_datazone.types.owner_properties_output.deserialize_json(item))
    return out
