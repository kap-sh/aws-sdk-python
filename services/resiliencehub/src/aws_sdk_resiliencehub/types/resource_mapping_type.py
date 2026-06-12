"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceMappingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ResourceMappingType: TypeAlias = Literal[
    "CfnStack",
    "Resource",
    "AppRegistryApp",
    "ResourceGroup",
    "Terraform",
    "EKS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CfnStack",
        "Resource",
        "AppRegistryApp",
        "ResourceGroup",
        "Terraform",
        "EKS",
    )
)


def serialize_json(value: ResourceMappingType) -> str:
    return value


def deserialize_json(data: str) -> ResourceMappingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceMappingType value: {data!r}")
    return cast(ResourceMappingType, data)
