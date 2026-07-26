"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceMappingType``."""

from typing import Literal, TypeAlias, cast

ResourceMappingType: TypeAlias = Literal[
    "CfnStack",
    "Resource",
    "AppRegistryApp",
    "ResourceGroup",
    "Terraform",
    "EKS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMappingType) -> str:
    return value


def deserialize_json(data: str) -> ResourceMappingType:
    return cast(ResourceMappingType, data)
