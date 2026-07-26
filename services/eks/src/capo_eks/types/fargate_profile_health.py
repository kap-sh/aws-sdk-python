"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.fargate_profile_issue_list


class FargateProfileHealth(TypedDict, closed=True):
    issues: NotRequired[
        "capo_eks.types.fargate_profile_issue_list.FargateProfileIssueList"
    ]
    """<p>Any issues that are associated with the Fargate profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfileHealth) -> dict:
    out: dict = {}
    if "issues" in value:
        import capo_eks.types.fargate_profile_issue_list

        out["issues"] = capo_eks.types.fargate_profile_issue_list.serialize_json(
            value["issues"]
        )
    return out


def deserialize_json(data: dict) -> FargateProfileHealth:
    out: FargateProfileHealth = {}  # type: ignore[typeddict-item]
    if "issues" in data:
        import capo_eks.types.fargate_profile_issue_list

        out["issues"] = capo_eks.types.fargate_profile_issue_list.deserialize_json(
            data["issues"]
        )
    return out
