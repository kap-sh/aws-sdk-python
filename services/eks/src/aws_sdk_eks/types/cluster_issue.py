"""Generated from Smithy shape ``com.amazonaws.eks#ClusterIssue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.cluster_issue_code
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class ClusterIssue(TypedDict):
    code: NotRequired["aws_sdk_eks.types.cluster_issue_code.ClusterIssueCode"]
    """<p>The error code of the issue.</p>"""
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A description of the issue.</p>"""
    resource_ids: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The resource IDs that the issue relates to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterIssue) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_eks.types.cluster_issue_code

        out["code"] = aws_sdk_eks.types.cluster_issue_code.serialize_json(value["code"])
    if "message" in value:
        out["message"] = value["message"]
    if "resource_ids" in value:
        import aws_sdk_eks.types.string_list

        out["resourceIds"] = aws_sdk_eks.types.string_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> ClusterIssue:
    out: ClusterIssue = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_eks.types.cluster_issue_code

        out["code"] = aws_sdk_eks.types.cluster_issue_code.deserialize_json(
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
