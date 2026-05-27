"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_ipam_operating_region_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_metered_account
    import aws_sdk_ec2.types.ipam_tier
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateIpamRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the IPAM.</p>"""
    operating_regions: NotRequired[
        "aws_sdk_ec2.types.add_ipam_operating_region_set.AddIpamOperatingRegionSet"
    ]
    """<p>The operating Regions for the IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions. </p> <p>For more information about operating Regions, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html\">Create an IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    tier: NotRequired["aws_sdk_ec2.types.ipam_tier.IpamTier"]
    """<p>IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and the costs associated with the tiers, see <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing > IPAM tab</a>.</p>"""
    enable_private_gua: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default.</p>"""
    metered_account: NotRequired[
        "aws_sdk_ec2.types.ipam_metered_account.IpamMeteredAccount"
    ]
    """<p>A metered account is an Amazon Web Services account that is charged for active IP addresses managed in IPAM. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html\">Enable cost distribution</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <p>Possible values:</p> <ul> <li> <p> <code>ipam-owner</code> (default): The Amazon Web Services account which owns the IPAM is charged for all active IP addresses managed in IPAM.</p> </li> <li> <p> <code>resource-owner</code>: The Amazon Web Services account that owns the IP address is charged for the active IP address.</p> </li> </ul>"""
