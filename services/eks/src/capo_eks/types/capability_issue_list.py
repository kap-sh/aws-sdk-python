"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityIssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.capability_issue

CapabilityIssueList: TypeAlias = list["capo_eks.types.capability_issue.CapabilityIssue"]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityIssueList) -> list:
    import capo_eks.types.capability_issue

    out: list = []
    for item in value:
        out.append(capo_eks.types.capability_issue.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapabilityIssueList:
    import capo_eks.types.capability_issue

    out: CapabilityIssueList = []
    for item in data:
        out.append(capo_eks.types.capability_issue.deserialize_json(item))
    return out
