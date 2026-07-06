"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageEksClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.addon_details
    import aws_sdk_guardduty.types.long
    import aws_sdk_guardduty.types.management_type
    import aws_sdk_guardduty.types.string


class CoverageEksClusterDetails(TypedDict, closed=True):
    cluster_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Name of the EKS cluster.</p>"""
    covered_nodes: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>Represents the nodes within the EKS cluster that have a <code>HEALTHY</code> coverage status.</p>"""
    compatible_nodes: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>Represents all the nodes within the EKS cluster in your account.</p>"""
    addon_details: NotRequired["aws_sdk_guardduty.types.addon_details.AddonDetails"]
    """<p>Information about the installed EKS add-on.</p>"""
    management_type: NotRequired[
        "aws_sdk_guardduty.types.management_type.ManagementType"
    ]
    """<p>Indicates how the Amazon EKS add-on GuardDuty agent is managed for this EKS cluster.</p> <p> <code>AUTO_MANAGED</code> indicates GuardDuty deploys and manages updates for this resource.</p> <p> <code>MANUAL</code> indicates that you are responsible to deploy, update, and manage the Amazon EKS add-on GuardDuty agent for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageEksClusterDetails) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "covered_nodes" in value:
        out["coveredNodes"] = value["covered_nodes"]
    if "compatible_nodes" in value:
        out["compatibleNodes"] = value["compatible_nodes"]
    if "addon_details" in value:
        import aws_sdk_guardduty.types.addon_details

        out["addonDetails"] = aws_sdk_guardduty.types.addon_details.serialize_json(
            value["addon_details"]
        )
    if "management_type" in value:
        import aws_sdk_guardduty.types.management_type

        out["managementType"] = aws_sdk_guardduty.types.management_type.serialize_json(
            value["management_type"]
        )
    return out


def deserialize_json(data: dict) -> CoverageEksClusterDetails:
    out: CoverageEksClusterDetails = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "coveredNodes" in data:
        out["covered_nodes"] = data["coveredNodes"]
    if "compatibleNodes" in data:
        out["compatible_nodes"] = data["compatibleNodes"]
    if "addonDetails" in data:
        import aws_sdk_guardduty.types.addon_details

        out["addon_details"] = aws_sdk_guardduty.types.addon_details.deserialize_json(
            data["addonDetails"]
        )
    if "managementType" in data:
        import aws_sdk_guardduty.types.management_type

        out["management_type"] = (
            aws_sdk_guardduty.types.management_type.deserialize_json(
                data["managementType"]
            )
        )
    return out
