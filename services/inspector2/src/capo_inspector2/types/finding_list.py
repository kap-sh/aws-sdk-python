"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.finding

FindingList: TypeAlias = list["capo_inspector2.types.finding.Finding"]


# --- restJson1 ser/de ---
def serialize_json(value: FindingList) -> list:
    import capo_inspector2.types.finding

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingList:
    import capo_inspector2.types.finding

    out: FindingList = []
    for item in data:
        out.append(capo_inspector2.types.finding.deserialize_json(item))
    return out
