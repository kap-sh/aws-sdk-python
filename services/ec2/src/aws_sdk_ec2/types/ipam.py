"""Generated from Smithy shape ``com.amazonaws.ec2#Ipam``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.ipam_metered_account
    import aws_sdk_ec2.types.ipam_operating_region_set
    import aws_sdk_ec2.types.ipam_resource_discovery_association_id
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.ipam_state
    import aws_sdk_ec2.types.ipam_tier
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class Ipam(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the IPAM.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the IPAM.</p>"""
    public_default_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the IPAM's default public scope.</p>"""
    private_default_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the IPAM's default private scope.</p>"""
    scope_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of scopes in the IPAM. The scope quota is 5. For more information on quotas, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html\">Quotas in IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the IPAM.</p>"""
    operating_regions: NotRequired[
        "aws_sdk_ec2.types.ipam_operating_region_set.IpamOperatingRegionSet"
    ]
    """<p>The operating Regions for an IPAM. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p> <p>For more information about operating Regions, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html\">Create an IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    state: NotRequired["aws_sdk_ec2.types.ipam_state.IpamState"]
    """<p>The state of the IPAM.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
    default_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The IPAM's default resource discovery ID.</p>"""
    default_resource_discovery_association_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association_id.IpamResourceDiscoveryAssociationId"
    ]
    """<p>The IPAM's default resource discovery association ID.</p>"""
    resource_discovery_association_count: NotRequired[
        "aws_sdk_ec2.types.integer.Integer"
    ]
    """<p>The IPAM's resource discovery association count.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state message.</p>"""
    tier: NotRequired["aws_sdk_ec2.types.ipam_tier.IpamTier"]
    """<p>IPAM is offered in a Free Tier and an Advanced Tier. For more information about the features available in each tier and the costs associated with the tiers, see <a href=\"http://aws.amazon.com/vpc/pricing/\">Amazon VPC pricing > IPAM tab</a>.</p>"""
    enable_private_gua: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enable this option to use your own GUA ranges as private IPv6 addresses. This option is disabled by default.</p>"""
    metered_account: NotRequired[
        "aws_sdk_ec2.types.ipam_metered_account.IpamMeteredAccount"
    ]
    """<p>A metered account is an Amazon Web Services account that is charged for active IP addresses managed in IPAM. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/ipam-enable-cost-distro.html\">Enable cost distribution</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <p>Possible values:</p> <ul> <li> <p> <code>ipam-owner</code> (default): The Amazon Web Services account which owns the IPAM is charged for all active IP addresses managed in IPAM.</p> </li> <li> <p> <code>resource-owner</code>: The Amazon Web Services account that owns the IP address is charged for the active IP address.</p> </li> </ul>"""
