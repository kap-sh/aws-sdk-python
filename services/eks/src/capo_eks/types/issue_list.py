"""Generated from Smithy shape ``com.amazonaws.eks#IssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.issue

IssueList: TypeAlias = list["capo_eks.types.issue.Issue"]


# --- restJson1 ser/de ---
def serialize_json(value: IssueList) -> list:
    import capo_eks.types.issue

    out: list = []
    for item in value:
        out.append(capo_eks.types.issue.serialize_json(item))
    return out


def deserialize_json(data: list) -> IssueList:
    import capo_eks.types.issue

    out: IssueList = []
    for item in data:
        out.append(capo_eks.types.issue.deserialize_json(item))
    return out
