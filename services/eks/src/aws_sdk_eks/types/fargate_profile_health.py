"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileHealth``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.fargate_profile_issue_list


class FargateProfileHealth(TypedDict):
    issues: NotRequired[
        "aws_sdk_eks.types.fargate_profile_issue_list.FargateProfileIssueList"
    ]
    """<p>Any issues that are associated with the Fargate profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfileHealth) -> dict:
    out: dict = {}
    if "issues" in value:
        import aws_sdk_eks.types.fargate_profile_issue_list

        out["issues"] = aws_sdk_eks.types.fargate_profile_issue_list.serialize_json(
            value["issues"]
        )
    return out


def deserialize_json(data: dict) -> FargateProfileHealth:
    out: FargateProfileHealth = {}  # type: ignore[typeddict-item]
    if "issues" in data:
        import aws_sdk_eks.types.fargate_profile_issue_list

        out["issues"] = aws_sdk_eks.types.fargate_profile_issue_list.deserialize_json(
            data["issues"]
        )
    return out
