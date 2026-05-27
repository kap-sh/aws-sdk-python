"""Generated from Smithy shape ``com.amazonaws.eks#IssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.issue

IssueList: TypeAlias = list["aws_sdk_eks.types.issue.Issue"]


# --- restJson1 ser/de ---
def serialize_json(value: IssueList) -> list:
    import aws_sdk_eks.types.issue

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.issue.serialize_json(item))
    return out


def deserialize_json(data: list) -> IssueList:
    import aws_sdk_eks.types.issue

    out: IssueList = []
    for item in data:
        out.append(aws_sdk_eks.types.issue.deserialize_json(item))
    return out
