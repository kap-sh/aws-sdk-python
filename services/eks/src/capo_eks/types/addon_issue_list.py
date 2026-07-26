"""Generated from Smithy shape ``com.amazonaws.eks#AddonIssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.addon_issue

AddonIssueList: TypeAlias = list["capo_eks.types.addon_issue.AddonIssue"]


# --- restJson1 ser/de ---
def serialize_json(value: AddonIssueList) -> list:
    import capo_eks.types.addon_issue

    out: list = []
    for item in value:
        out.append(capo_eks.types.addon_issue.serialize_json(item))
    return out


def deserialize_json(data: list) -> AddonIssueList:
    import capo_eks.types.addon_issue

    out: AddonIssueList = []
    for item in data:
        out.append(capo_eks.types.addon_issue.deserialize_json(item))
    return out
