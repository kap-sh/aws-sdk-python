"""Generated from Smithy shape ``com.amazonaws.auditmanager#EvidenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.evidence

EvidenceList: TypeAlias = list["aws_sdk_auditmanager.types.evidence.Evidence"]


# --- restJson1 ser/de ---
def serialize_json(value: EvidenceList) -> list:
    import aws_sdk_auditmanager.types.evidence

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.evidence.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvidenceList:
    import aws_sdk_auditmanager.types.evidence

    out: EvidenceList = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.evidence.deserialize_json(item))
    return out
