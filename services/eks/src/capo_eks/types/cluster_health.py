"""Generated from Smithy shape ``com.amazonaws.eks#ClusterHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.cluster_issue_list


class ClusterHealth(TypedDict, closed=True):
    issues: NotRequired["capo_eks.types.cluster_issue_list.ClusterIssueList"]
    """<p>An object representing the health issues of your Amazon EKS cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterHealth) -> dict:
    out: dict = {}
    if "issues" in value:
        import capo_eks.types.cluster_issue_list

        out["issues"] = capo_eks.types.cluster_issue_list.serialize_json(
            value["issues"]
        )
    return out


def deserialize_json(data: dict) -> ClusterHealth:
    out: ClusterHealth = {}  # type: ignore[typeddict-item]
    if "issues" in data:
        import capo_eks.types.cluster_issue_list

        out["issues"] = capo_eks.types.cluster_issue_list.deserialize_json(
            data["issues"]
        )
    return out
