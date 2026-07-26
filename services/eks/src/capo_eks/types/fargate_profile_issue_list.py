"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileIssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.fargate_profile_issue

FargateProfileIssueList: TypeAlias = list[
    "capo_eks.types.fargate_profile_issue.FargateProfileIssue"
]


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfileIssueList) -> list:
    import capo_eks.types.fargate_profile_issue

    out: list = []
    for item in value:
        out.append(capo_eks.types.fargate_profile_issue.serialize_json(item))
    return out


def deserialize_json(data: list) -> FargateProfileIssueList:
    import capo_eks.types.fargate_profile_issue

    out: FargateProfileIssueList = []
    for item in data:
        out.append(capo_eks.types.fargate_profile_issue.deserialize_json(item))
    return out
