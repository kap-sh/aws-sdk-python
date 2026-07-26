"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.control_metadata

ControlMetadataList: TypeAlias = list[
    "capo_auditmanager.types.control_metadata.ControlMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlMetadataList) -> list:
    import capo_auditmanager.types.control_metadata

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.control_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlMetadataList:
    import capo_auditmanager.types.control_metadata

    out: ControlMetadataList = []
    for item in data:
        out.append(capo_auditmanager.types.control_metadata.deserialize_json(item))
    return out
