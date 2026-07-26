"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.capability_issue_list


class CapabilityHealth(TypedDict, closed=True):
    issues: NotRequired["capo_eks.types.capability_issue_list.CapabilityIssueList"]
    """<p>A list of issues affecting the capability. If this list is empty, the capability is healthy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityHealth) -> dict:
    out: dict = {}
    if "issues" in value:
        import capo_eks.types.capability_issue_list

        out["issues"] = capo_eks.types.capability_issue_list.serialize_json(
            value["issues"]
        )
    return out


def deserialize_json(data: dict) -> CapabilityHealth:
    out: CapabilityHealth = {}  # type: ignore[typeddict-item]
    if "issues" in data:
        import capo_eks.types.capability_issue_list

        out["issues"] = capo_eks.types.capability_issue_list.deserialize_json(
            data["issues"]
        )
    return out
