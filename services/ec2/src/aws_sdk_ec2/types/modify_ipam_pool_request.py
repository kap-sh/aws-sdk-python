"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPoolRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_netmask_length
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.request_ipam_resource_tag_list
    import aws_sdk_ec2.types.string


class ModifyIpamPoolRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool you want to modify.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the IPAM pool you want to modify.</p>"""
    auto_import: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If true, IPAM will continuously look for resources within the CIDR range of this pool and automatically import them as allocations into your IPAM. The CIDRs that will be allocated for these resources must not already be allocated to other resources in order for the import to succeed. IPAM will import a CIDR regardless of its compliance with the pool's allocation rules, so a resource might be imported and subsequently marked as noncompliant. If IPAM discovers multiple CIDRs that overlap, IPAM will import the largest CIDR only. If IPAM discovers multiple CIDRs with matching CIDRs, IPAM will randomly import one of them only. </p> <p>A locale must be set on the pool for this feature to work.</p>"""
    allocation_min_netmask_length: NotRequired[
        "aws_sdk_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The minimum netmask length required for CIDR allocations in this IPAM pool to be compliant. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128. The minimum netmask length must be less than the maximum netmask length.</p>"""
    allocation_max_netmask_length: NotRequired[
        "aws_sdk_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The maximum netmask length possible for CIDR allocations in this IPAM pool to be compliant. Possible netmask lengths for IPv4 addresses are 0 - 32. Possible netmask lengths for IPv6 addresses are 0 - 128.The maximum netmask length must be greater than the minimum netmask length.</p>"""
    allocation_default_netmask_length: NotRequired[
        "aws_sdk_ec2.types.ipam_netmask_length.IpamNetmaskLength"
    ]
    """<p>The default netmask length for allocations added to this pool. If, for example, the CIDR assigned to this pool is 10.0.0.0/8 and you enter 16 here, new allocations will default to 10.0.0.0/16.</p>"""
    clear_allocation_default_netmask_length: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Clear the default netmask length allocation rule for this pool.</p>"""
    add_allocation_resource_tags: NotRequired[
        "aws_sdk_ec2.types.request_ipam_resource_tag_list.RequestIpamResourceTagList"
    ]
    """<p>Add tag allocation rules to a pool. For more information about allocation rules, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/create-top-ipam.html\">Create a top-level pool</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    remove_allocation_resource_tags: NotRequired[
        "aws_sdk_ec2.types.request_ipam_resource_tag_list.RequestIpamResourceTagList"
    ]
    """<p>Remove tag allocation rules from a pool.</p>"""
