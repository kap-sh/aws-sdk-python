"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid

EvidenceIds: TypeAlias = list["aws_sdk_auditmanager.types.uuid.UUID"]


# --- restJson1 ser/de ---
def serialize_json(value: EvidenceIds) -> list:
    return list(value)


def deserialize_json(data: list) -> EvidenceIds:
    return list(data)
