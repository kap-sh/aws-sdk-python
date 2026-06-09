"""Generated from Smithy shape ``com.amazonaws.eks#AddonInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.addon_version_info_list
    import aws_sdk_eks.types.marketplace_information
    import aws_sdk_eks.types.string


class AddonInfo(TypedDict):
    addon_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the add-on.</p>"""
    type: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The type of the add-on.</p>"""
    addon_versions: NotRequired[
        "aws_sdk_eks.types.addon_version_info_list.AddonVersionInfoList"
    ]
    """<p>An object representing information about available add-on versions and compatible Kubernetes versions.</p>"""
    publisher: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The publisher of the add-on.</p>"""
    owner: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The owner of the add-on.</p>"""
    marketplace_information: NotRequired[
        "aws_sdk_eks.types.marketplace_information.MarketplaceInformation"
    ]
    """<p>Information about the add-on from the Amazon Web Services Marketplace.</p>"""
    default_namespace: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The default Kubernetes namespace where this addon is typically installed if no custom namespace is specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddonInfo) -> dict:
    out: dict = {}
    if "addon_name" in value:
        out["addonName"] = value["addon_name"]
    if "type" in value:
        out["type"] = value["type"]
    if "addon_versions" in value:
        import aws_sdk_eks.types.addon_version_info_list

        out["addonVersions"] = aws_sdk_eks.types.addon_version_info_list.serialize_json(
            value["addon_versions"]
        )
    if "publisher" in value:
        out["publisher"] = value["publisher"]
    if "owner" in value:
        out["owner"] = value["owner"]
    if "marketplace_information" in value:
        import aws_sdk_eks.types.marketplace_information

        out["marketplaceInformation"] = (
            aws_sdk_eks.types.marketplace_information.serialize_json(
                value["marketplace_information"]
            )
        )
    if "default_namespace" in value:
        out["defaultNamespace"] = value["default_namespace"]
    return out


def deserialize_json(data: dict) -> AddonInfo:
    out: AddonInfo = {}  # type: ignore[typeddict-item]
    if "addonName" in data:
        out["addon_name"] = data["addonName"]
    if "type" in data:
        out["type"] = data["type"]
    if "addonVersions" in data:
        import aws_sdk_eks.types.addon_version_info_list

        out["addon_versions"] = (
            aws_sdk_eks.types.addon_version_info_list.deserialize_json(
                data["addonVersions"]
            )
        )
    if "publisher" in data:
        out["publisher"] = data["publisher"]
    if "owner" in data:
        out["owner"] = data["owner"]
    if "marketplaceInformation" in data:
        import aws_sdk_eks.types.marketplace_information

        out["marketplace_information"] = (
            aws_sdk_eks.types.marketplace_information.deserialize_json(
                data["marketplaceInformation"]
            )
        )
    if "defaultNamespace" in data:
        out["default_namespace"] = data["defaultNamespace"]
    return out
