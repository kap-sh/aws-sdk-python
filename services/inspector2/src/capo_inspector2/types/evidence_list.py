"""Generated from Smithy shape ``com.amazonaws.inspector2#EvidenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.evidence

EvidenceList: TypeAlias = list["capo_inspector2.types.evidence.Evidence"]


# --- restJson1 ser/de ---
def serialize_json(value: EvidenceList) -> list:
    import capo_inspector2.types.evidence

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.evidence.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvidenceList:
    import capo_inspector2.types.evidence

    out: EvidenceList = []
    for item in data:
        out.append(capo_inspector2.types.evidence.deserialize_json(item))
    return out
