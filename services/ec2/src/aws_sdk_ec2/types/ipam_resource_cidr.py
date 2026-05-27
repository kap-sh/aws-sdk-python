"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceCidr``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boxed_double
    import aws_sdk_ec2.types.ipam_compliance_status
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.ipam_management_state
    import aws_sdk_ec2.types.ipam_overlap_status
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.ipam_resource_tag_list
    import aws_sdk_ec2.types.ipam_resource_type
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.string


class IpamResourceCidr(TypedDict):
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The IPAM ID for an IPAM resource.</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The scope ID for an IPAM resource.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The pool ID for an IPAM resource.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region for an IPAM resource.</p>"""
    resource_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account number of the owner of an IPAM resource.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of an IPAM resource.</p>"""
    resource_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of an IPAM resource.</p>"""
    resource_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR for an IPAM resource.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>The type of IPAM resource.</p>"""
    resource_tags: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_tag_list.IpamResourceTagList"
    ]
    """<p>The tags for an IPAM resource.</p>"""
    ip_usage: NotRequired["aws_sdk_ec2.types.boxed_double.BoxedDouble"]
    """<p>The percentage of IP address space in use. To convert the decimal to a percentage, multiply the decimal by 100. Note the following:</p> <ul> <li> <p>For resources that are VPCs, this is the percentage of IP address space in the VPC that's taken up by subnet CIDRs. </p> </li> <li> <p>For resources that are subnets, if the subnet has an IPv4 CIDR provisioned to it, this is the percentage of IPv4 address space in the subnet that's in use. If the subnet has an IPv6 CIDR provisioned to it, the percentage of IPv6 address space in use is not represented. The percentage of IPv6 address space in use cannot currently be calculated. </p> </li> <li> <p>For resources that are public IPv4 pools, this is the percentage of IP address space in the pool that's been allocated to Elastic IP addresses (EIPs). </p> </li> </ul>"""
    compliance_status: NotRequired[
        "aws_sdk_ec2.types.ipam_compliance_status.IpamComplianceStatus"
    ]
    """<p>The compliance status of the IPAM resource. For more information on compliance statuses, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html\">Monitor CIDR usage by resource</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    management_state: NotRequired[
        "aws_sdk_ec2.types.ipam_management_state.IpamManagementState"
    ]
    """<p>The management state of the resource. For more information about management states, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html\">Monitor CIDR usage by resource</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    overlap_status: NotRequired[
        "aws_sdk_ec2.types.ipam_overlap_status.IpamOverlapStatus"
    ]
    """<p>The overlap status of an IPAM resource. The overlap status tells you if the CIDR for a resource overlaps with another CIDR in the scope. For more information on overlap statuses, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html\">Monitor CIDR usage by resource</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of a VPC.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone ID.</p>"""
