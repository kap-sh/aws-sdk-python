"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.issue_list


class NodegroupHealth(TypedDict, closed=True):
    issues: NotRequired["capo_eks.types.issue_list.IssueList"]
    """<p>Any issues that are associated with the node group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodegroupHealth) -> dict:
    out: dict = {}
    if "issues" in value:
        import capo_eks.types.issue_list

        out["issues"] = capo_eks.types.issue_list.serialize_json(value["issues"])
    return out


def deserialize_json(data: dict) -> NodegroupHealth:
    out: NodegroupHealth = {}  # type: ignore[typeddict-item]
    if "issues" in data:
        import capo_eks.types.issue_list

        out["issues"] = capo_eks.types.issue_list.deserialize_json(data["issues"])
    return out
