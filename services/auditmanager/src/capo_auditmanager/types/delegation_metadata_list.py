"""Generated from Smithy shape ``com.amazonaws.auditmanager#DelegationMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.delegation_metadata

DelegationMetadataList: TypeAlias = list[
    "capo_auditmanager.types.delegation_metadata.DelegationMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: DelegationMetadataList) -> list:
    import capo_auditmanager.types.delegation_metadata

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.delegation_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> DelegationMetadataList:
    import capo_auditmanager.types.delegation_metadata

    out: DelegationMetadataList = []
    for item in data:
        out.append(capo_auditmanager.types.delegation_metadata.deserialize_json(item))
    return out
