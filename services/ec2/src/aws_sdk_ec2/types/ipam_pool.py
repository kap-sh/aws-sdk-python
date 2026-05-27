"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPool``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_family
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipam_netmask_length
    import aws_sdk_ec2.types.ipam_pool_aws_service
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.ipam_pool_public_ip_source
    import aws_sdk_ec2.types.ipam_pool_source_resource
    import aws_sdk_ec2.types.ipam_pool_state
    import aws_sdk_ec2.types.ipam_resource_tag_list
    import aws_sdk_ec2.types.ipam_scope_type
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamPool(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the IPAM pool.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool.</p>"""
    source_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the source IPAM pool. You can use this option to create an IPAM pool within an existing source pool.</p>"""
    ipam_pool_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM pool.</p>"""
    ipam_scope_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the scope of the IPAM pool.</p>"""
    ipam_scope_type: NotRequired["aws_sdk_ec2.types.ipam_scope_type.IpamScopeType"]
    """<p>In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the IPAM.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the IPAM pool.</p>"""
    locale: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The locale of the IPAM pool.</p> <p>The locale for the pool should be one of the following:</p> <ul> <li> <p>An Amazon Web Services Region where you want this IPAM pool to be available for allocations.</p> </li> <li> <p>The network border group for an Amazon Web Services Local Zone where you want this IPAM pool to be available for allocations (<a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-zone-avail\">supported Local Zones</a>). This option is only available for IPAM IPv4 pools in the public scope.</p> </li> </ul> <p>If you choose an Amazon Web Services Region for locale that has not been configured as an operating Region for the IPAM, you'll get an error.</p>"""
    pool_depth: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The depth of pools in your IPAM pool. The pool depth quota is 10. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html\">Quotas in IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    state: NotRequired["aws_sdk_ec2.types.ipam_pool_state.IpamPoolState"]
    """<p>The state of the IPAM pool.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state message.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the IPAM pool.</p>"""
    auto_import: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If selected, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only. </p> <p>A locale must be set on the pool for this feature to work.</p>"""
    publicly_advertisable: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Determines if a pool is publicly advertisable. This option is not available for pools with AddressFamily set to <code>ipv4</code>.</p>"""
    address_family: NotRequired["aws_sdk_ec2.types.address_family.AddressFamily"]
    """<p>The address family of the pool.</p>"""
    allocation_min_netmask_length: NotRequired[
        "aws_sdk_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. The minimum netmask length must be less than the maximum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.</p>"""
    allocation_max_netmask_length: NotRequired[
        "aws_sdk_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. The maximum netmask length must be greater than the minimum netmask length. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.</p>"""
    allocation_default_netmask_length: NotRequired[
        "aws_sdk_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.</p>"""
    allocation_resource_tags: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_tag_list.IpamResourceTagList"
    ]
    """<p>Tags that are required for resources that use CIDRs from this IPAM pool. Resources that do not have these tags will not be allowed to allocate space from the pool. If the resources have their tags changed after they have allocated space or if the allocation tagging requirements are changed on the pool, the resource may be marked as noncompliant.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
    aws_service: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_aws_service.IpamPoolAwsService"
    ]
    """<p>Limits which service in Amazon Web Services that the pool can be used in. \"ec2\", for example, allows users to use space for Elastic IP addresses and VPCs.</p>"""
    public_ip_source: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_public_ip_source.IpamPoolPublicIpSource"
    ]
    """<p>The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is <code>BYOIP</code>. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/intro-create-ipv6-pools.html\">Create IPv6 pools</a> in the <i>Amazon VPC IPAM User Guide</i>. By default, you can add only one Amazon-provided IPv6 CIDR block to a top-level IPv6 pool. For information on increasing the default limit, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html\">Quotas for your IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    source_resource: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_source_resource.IpamPoolSourceResource"
    ]
    """<p>The resource used to provision CIDRs to a resource planning pool.</p>"""
