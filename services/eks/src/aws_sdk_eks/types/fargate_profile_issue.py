"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileIssue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.fargate_profile_issue_code
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class FargateProfileIssue(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_eks.types.fargate_profile_issue_code.FargateProfileIssueCode"
    ]
    """<p>A brief description of the error.</p>"""
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The error message associated with the issue.</p>"""
    resource_ids: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The Amazon Web Services resources that are affected by this issue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FargateProfileIssue) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_eks.types.fargate_profile_issue_code

        out["code"] = aws_sdk_eks.types.fargate_profile_issue_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "resource_ids" in value:
        import aws_sdk_eks.types.string_list

        out["resourceIds"] = aws_sdk_eks.types.string_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> FargateProfileIssue:
    out: FargateProfileIssue = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_eks.types.fargate_profile_issue_code

        out["code"] = aws_sdk_eks.types.fargate_profile_issue_code.deserialize_json(
            data["code"]
        )
    if "message" in data:
        out["message"] = data["message"]
    if "resourceIds" in data:
        import aws_sdk_eks.types.string_list

        out["resource_ids"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["resourceIds"]
        )
    return out
