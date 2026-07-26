"""Generated from Smithy shape ``com.amazonaws.auditmanager#ServiceMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.service_metadata

ServiceMetadataList: TypeAlias = list[
    "capo_auditmanager.types.service_metadata.ServiceMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceMetadataList) -> list:
    import capo_auditmanager.types.service_metadata

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.service_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceMetadataList:
    import capo_auditmanager.types.service_metadata

    out: ServiceMetadataList = []
    for item in data:
        out.append(capo_auditmanager.types.service_metadata.deserialize_json(item))
    return out
