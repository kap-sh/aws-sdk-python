"""Generated from Smithy shape ``com.amazonaws.securityhub#RelatedFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.related_finding

RelatedFindingList: TypeAlias = list[
    "capo_securityhub.types.related_finding.RelatedFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedFindingList) -> list:
    import capo_securityhub.types.related_finding

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.related_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> RelatedFindingList:
    import capo_securityhub.types.related_finding

    out: RelatedFindingList = []
    for item in data:
        out.append(capo_securityhub.types.related_finding.deserialize_json(item))
    return out
