"""Generated from Smithy shape ``com.amazonaws.eks#ClusterIssue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.cluster_issue_code
    import capo_eks.types.string
    import capo_eks.types.string_list


class ClusterIssue(TypedDict, closed=True):
    code: NotRequired["capo_eks.types.cluster_issue_code.ClusterIssueCode"]
    """<p>The error code of the issue.</p>"""
    message: NotRequired["capo_eks.types.string.String"]
    """<p>A description of the issue.</p>"""
    resource_ids: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The resource IDs that the issue relates to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterIssue) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_eks.types.cluster_issue_code

        out["code"] = capo_eks.types.cluster_issue_code.serialize_json(value["code"])
    if "message" in value:
        out["message"] = value["message"]
    if "resource_ids" in value:
        import capo_eks.types.string_list

        out["resourceIds"] = capo_eks.types.string_list.serialize_json(
            value["resource_ids"]
        )
    return out


def deserialize_json(data: dict) -> ClusterIssue:
    out: ClusterIssue = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import capo_eks.types.cluster_issue_code

        out["code"] = capo_eks.types.cluster_issue_code.deserialize_json(data["code"])
    if "message" in data:
        out["message"] = data["message"]
    if "resourceIds" in data:
        import capo_eks.types.string_list

        out["resource_ids"] = capo_eks.types.string_list.deserialize_json(
            data["resourceIds"]
        )
    return out
