"""Generated from Smithy shape ``com.amazonaws.eks#AddonHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.addon_issue_list


class AddonHealth(TypedDict, closed=True):
    issues: NotRequired["capo_eks.types.addon_issue_list.AddonIssueList"]
    """<p>An object representing the health issues for an add-on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonHealth) -> dict:
    out: dict = {}
    if "issues" in value:
        import capo_eks.types.addon_issue_list

        out["issues"] = capo_eks.types.addon_issue_list.serialize_json(value["issues"])
    return out


def deserialize_json(data: dict) -> AddonHealth:
    out: AddonHealth = {}  # type: ignore[typeddict-item]
    if "issues" in data:
        import capo_eks.types.addon_issue_list

        out["issues"] = capo_eks.types.addon_issue_list.deserialize_json(data["issues"])
    return out
