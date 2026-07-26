"""Generated from Smithy shape ``com.amazonaws.sesv2#ResourceTenantMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.resource_tenant_metadata

ResourceTenantMetadataList: TypeAlias = list[
    "capo_sesv2.types.resource_tenant_metadata.ResourceTenantMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTenantMetadataList) -> list:
    import capo_sesv2.types.resource_tenant_metadata

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.resource_tenant_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTenantMetadataList:
    import capo_sesv2.types.resource_tenant_metadata

    out: ResourceTenantMetadataList = []
    for item in data:
        out.append(capo_sesv2.types.resource_tenant_metadata.deserialize_json(item))
    return out
