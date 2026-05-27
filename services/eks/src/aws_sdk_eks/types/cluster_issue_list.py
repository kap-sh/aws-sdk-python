"""Generated from Smithy shape ``com.amazonaws.eks#ClusterIssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.cluster_issue

ClusterIssueList: TypeAlias = list["aws_sdk_eks.types.cluster_issue.ClusterIssue"]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterIssueList) -> list:
    import aws_sdk_eks.types.cluster_issue

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.cluster_issue.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterIssueList:
    import aws_sdk_eks.types.cluster_issue

    out: ClusterIssueList = []
    for item in data:
        out.append(aws_sdk_eks.types.cluster_issue.deserialize_json(item))
    return out
