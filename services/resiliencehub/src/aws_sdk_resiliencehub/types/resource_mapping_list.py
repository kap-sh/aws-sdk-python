"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resource_mapping

ResourceMappingList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.resource_mapping.ResourceMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMappingList) -> list:
    import aws_sdk_resiliencehub.types.resource_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.resource_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceMappingList:
    import aws_sdk_resiliencehub.types.resource_mapping

    out: ResourceMappingList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.resource_mapping.deserialize_json(item))
    return out
