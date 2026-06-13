"""Generated from Smithy shape ``com.amazonaws.omics#RegistryMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.registry_mapping

RegistryMappingsList: TypeAlias = list[
    "aws_sdk_omics.types.registry_mapping.RegistryMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryMappingsList) -> list:
    import aws_sdk_omics.types.registry_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.registry_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegistryMappingsList:
    import aws_sdk_omics.types.registry_mapping

    out: RegistryMappingsList = []
    for item in data:
        out.append(aws_sdk_omics.types.registry_mapping.deserialize_json(item))
    return out
