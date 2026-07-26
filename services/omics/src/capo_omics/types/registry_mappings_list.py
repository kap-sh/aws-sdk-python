"""Generated from Smithy shape ``com.amazonaws.omics#RegistryMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.registry_mapping

RegistryMappingsList: TypeAlias = list[
    "capo_omics.types.registry_mapping.RegistryMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryMappingsList) -> list:
    import capo_omics.types.registry_mapping

    out: list = []
    for item in value:
        out.append(capo_omics.types.registry_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegistryMappingsList:
    import capo_omics.types.registry_mapping

    out: RegistryMappingsList = []
    for item in data:
        out.append(capo_omics.types.registry_mapping.deserialize_json(item))
    return out
