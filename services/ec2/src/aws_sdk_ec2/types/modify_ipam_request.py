"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_ipam_operating_region_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.ipam_metered_account
    import aws_sdk_ec2.types.ipam_tier
    import aws_sdk_ec2.types.remove_ipam_operating_region_set
    import aws_sdk_ec2.types.string


class ModifyIpamRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM you want to modify.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the IPAM you want to modify.</p>"""
    add_operating_regions: NotRequired[
        "aws_sdk_ec2.types.add_ipam_operating_region_set.AddIpamOperatingRegionSet"
    ]
    """<p>Choose the operating Regions for the IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p> <p>For more information about operating Regions, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html\">Create an IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    remove_operating_regions: NotRequired[
        "aws_sdk_ec2.types.remove_ipam_operating_region_set.RemoveIpamOperatingRegionSet"
    ]
    """<p>The operating Regions to remove.</p>"""
    tier: NotRequired["aws_sdk_ec2.types.ipam_tier.IpamTier"]
    """<p>IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and the costs associated with the tiers, see <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing > IPAM tab</a>.</p>"""
    enable_private_gua: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default.</p>"""
    metered_account: NotRequired[
        "aws_sdk_ec2.types.ipam_metered_account.IpamMeteredAccount"
    ]
    """<p>A metered account is an Amazon Web Services account that is charged for active IP addresses managed in IPAM. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html\">Enable cost distribution</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <p>Possible values:</p> <ul> <li> <p> <code>ipam-owner</code> (default): The Amazon Web Services account which owns the IPAM is charged for all active IP addresses managed in IPAM.</p> </li> <li> <p> <code>resource-owner</code>: The Amazon Web Services account that owns the IP address is charged for the active IP address.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_id" in value:
        pairs.append((f"{prefix}.IpamId", str(value["ipam_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "add_operating_regions" in value:
        import aws_sdk_ec2.types.add_ipam_operating_region_set

        aws_sdk_ec2.types.add_ipam_operating_region_set.serialize_ec2_query(
            value["add_operating_regions"], pairs, f"{prefix}.AddOperatingRegions"
        )
    if "remove_operating_regions" in value:
        import aws_sdk_ec2.types.remove_ipam_operating_region_set

        aws_sdk_ec2.types.remove_ipam_operating_region_set.serialize_ec2_query(
            value["remove_operating_regions"], pairs, f"{prefix}.RemoveOperatingRegions"
        )
    if "tier" in value:
        import aws_sdk_ec2.types.ipam_tier

        aws_sdk_ec2.types.ipam_tier.serialize_ec2_query(
            value["tier"], pairs, f"{prefix}.Tier"
        )
    if "enable_private_gua" in value:
        pairs.append(
            (
                f"{prefix}.EnablePrivateGua",
                "true" if value["enable_private_gua"] else "false",
            )
        )
    if "metered_account" in value:
        import aws_sdk_ec2.types.ipam_metered_account

        aws_sdk_ec2.types.ipam_metered_account.serialize_ec2_query(
            value["metered_account"], pairs, f"{prefix}.MeteredAccount"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamRequest:
    out: ModifyIpamRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("AddOperatingRegions") is not None:
        import aws_sdk_ec2.types.add_ipam_operating_region_set

        out["add_operating_regions"] = (
            aws_sdk_ec2.types.add_ipam_operating_region_set.deserialize_ec2_query(
                el, "AddOperatingRegions"
            )
        )
    if el.find("RemoveOperatingRegions") is not None:
        import aws_sdk_ec2.types.remove_ipam_operating_region_set

        out["remove_operating_regions"] = (
            aws_sdk_ec2.types.remove_ipam_operating_region_set.deserialize_ec2_query(
                el, "RemoveOperatingRegions"
            )
        )
    child_tier = el.find("Tier")
    if child_tier is not None:
        import aws_sdk_ec2.types.ipam_tier

        out["tier"] = aws_sdk_ec2.types.ipam_tier.deserialize_ec2_query(child_tier)
    child_enable_private_gua = el.find("EnablePrivateGua")
    if child_enable_private_gua is not None:
        out["enable_private_gua"] = (
            child_enable_private_gua.text or ""
        ).lower() == "true"
    child_metered_account = el.find("MeteredAccount")
    if child_metered_account is not None:
        import aws_sdk_ec2.types.ipam_metered_account

        out["metered_account"] = (
            aws_sdk_ec2.types.ipam_metered_account.deserialize_ec2_query(
                child_metered_account
            )
        )
    return out
