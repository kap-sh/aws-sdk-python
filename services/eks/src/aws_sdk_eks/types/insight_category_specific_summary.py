"""Generated from Smithy shape ``com.amazonaws.eks#InsightCategorySpecificSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.addon_compatibility_details
    import aws_sdk_eks.types.deprecation_details


class InsightCategorySpecificSummary(TypedDict):
    deprecation_details: NotRequired[
        "aws_sdk_eks.types.deprecation_details.DeprecationDetails"
    ]
    """<p>The summary information about deprecated resource usage for an insight check in the <code>UPGRADE_READINESS</code> category.</p>"""
    addon_compatibility_details: NotRequired[
        "aws_sdk_eks.types.addon_compatibility_details.AddonCompatibilityDetails"
    ]
    """<p>A list of <code>AddonCompatibilityDetail</code> objects for Amazon EKS add-ons.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightCategorySpecificSummary) -> dict:
    out: dict = {}
    if "deprecation_details" in value:
        import aws_sdk_eks.types.deprecation_details

        out["deprecationDetails"] = (
            aws_sdk_eks.types.deprecation_details.serialize_json(
                value["deprecation_details"]
            )
        )
    if "addon_compatibility_details" in value:
        import aws_sdk_eks.types.addon_compatibility_details

        out["addonCompatibilityDetails"] = (
            aws_sdk_eks.types.addon_compatibility_details.serialize_json(
                value["addon_compatibility_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> InsightCategorySpecificSummary:
    out: InsightCategorySpecificSummary = {}  # type: ignore[typeddict-item]
    if "deprecationDetails" in data:
        import aws_sdk_eks.types.deprecation_details

        out["deprecation_details"] = (
            aws_sdk_eks.types.deprecation_details.deserialize_json(
                data["deprecationDetails"]
            )
        )
    if "addonCompatibilityDetails" in data:
        import aws_sdk_eks.types.addon_compatibility_details

        out["addon_compatibility_details"] = (
            aws_sdk_eks.types.addon_compatibility_details.deserialize_json(
                data["addonCompatibilityDetails"]
            )
        )
    return out
