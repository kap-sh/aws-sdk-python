"""Generated from Smithy shape ``com.amazonaws.eks#AddonCompatibilityDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.string_list


class AddonCompatibilityDetail(TypedDict, closed=True):
    name: NotRequired["capo_eks.types.string.String"]
    """<p>The name of the Amazon EKS add-on.</p>"""
    compatible_versions: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The list of compatible Amazon EKS add-on versions for the next Kubernetes version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonCompatibilityDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "compatible_versions" in value:
        import capo_eks.types.string_list

        out["compatibleVersions"] = capo_eks.types.string_list.serialize_json(
            value["compatible_versions"]
        )
    return out


def deserialize_json(data: dict) -> AddonCompatibilityDetail:
    out: AddonCompatibilityDetail = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "compatibleVersions" in data:
        import capo_eks.types.string_list

        out["compatible_versions"] = capo_eks.types.string_list.deserialize_json(
            data["compatibleVersions"]
        )
    return out
