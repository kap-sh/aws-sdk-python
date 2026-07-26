"""Generated from Smithy shape ``com.amazonaws.eks#AddonPodIdentityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.string_list


class AddonPodIdentityConfiguration(TypedDict, closed=True):
    service_account: NotRequired["capo_eks.types.string.String"]
    """<p>The Kubernetes Service Account name used by the add-on.</p>"""
    recommended_managed_policies: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>A suggested IAM Policy for the add-on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonPodIdentityConfiguration) -> dict:
    out: dict = {}
    if "service_account" in value:
        out["serviceAccount"] = value["service_account"]
    if "recommended_managed_policies" in value:
        import capo_eks.types.string_list

        out["recommendedManagedPolicies"] = capo_eks.types.string_list.serialize_json(
            value["recommended_managed_policies"]
        )
    return out


def deserialize_json(data: dict) -> AddonPodIdentityConfiguration:
    out: AddonPodIdentityConfiguration = {}  # type: ignore[typeddict-item]
    if "serviceAccount" in data:
        out["service_account"] = data["serviceAccount"]
    if "recommendedManagedPolicies" in data:
        import capo_eks.types.string_list

        out["recommended_managed_policies"] = (
            capo_eks.types.string_list.deserialize_json(
                data["recommendedManagedPolicies"]
            )
        )
    return out
