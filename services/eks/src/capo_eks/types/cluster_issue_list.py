"""Generated from Smithy shape ``com.amazonaws.eks#ClusterIssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.cluster_issue

ClusterIssueList: TypeAlias = list["capo_eks.types.cluster_issue.ClusterIssue"]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterIssueList) -> list:
    import capo_eks.types.cluster_issue

    out: list = []
    for item in value:
        out.append(capo_eks.types.cluster_issue.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterIssueList:
    import capo_eks.types.cluster_issue

    out: ClusterIssueList = []
    for item in data:
        out.append(capo_eks.types.cluster_issue.deserialize_json(item))
    return out
