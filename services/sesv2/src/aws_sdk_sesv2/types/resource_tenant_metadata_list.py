"""Generated from Smithy shape ``com.amazonaws.sesv2#ResourceTenantMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.resource_tenant_metadata

ResourceTenantMetadataList: TypeAlias = list[
    "aws_sdk_sesv2.types.resource_tenant_metadata.ResourceTenantMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTenantMetadataList) -> list:
    import aws_sdk_sesv2.types.resource_tenant_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.resource_tenant_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTenantMetadataList:
    import aws_sdk_sesv2.types.resource_tenant_metadata

    out: ResourceTenantMetadataList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.resource_tenant_metadata.deserialize_json(item))
    return out
