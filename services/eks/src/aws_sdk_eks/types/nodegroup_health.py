"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.issue_list


class NodegroupHealth(TypedDict, closed=True):
    issues: NotRequired["aws_sdk_eks.types.issue_list.IssueList"]
    """<p>Any issues that are associated with the node group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodegroupHealth) -> dict:
    out: dict = {}
    if "issues" in value:
        import aws_sdk_eks.types.issue_list

        out["issues"] = aws_sdk_eks.types.issue_list.serialize_json(value["issues"])
    return out


def deserialize_json(data: dict) -> NodegroupHealth:
    out: NodegroupHealth = {}  # type: ignore[typeddict-item]
    if "issues" in data:
        import aws_sdk_eks.types.issue_list

        out["issues"] = aws_sdk_eks.types.issue_list.deserialize_json(data["issues"])
    return out
