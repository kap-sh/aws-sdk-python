"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.ipv6_pool_ec2_id
    import aws_sdk_ec2.types.netmask_length
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.tenancy
    import aws_sdk_ec2.types.vpc_encryption_control_configuration


class CreateVpcRequest(TypedDict):
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 network range for the VPC, in CIDR notation. For example, <code>10.0.0.0/16</code>. We modify the specified CIDR block to its canonical form; for example, if you specify <code>100.68.0.18/18</code>, we modify it to <code>100.68.0.0/18</code>.</p>"""
    ipv6_pool: NotRequired["aws_sdk_ec2.types.ipv6_pool_ec2_id.Ipv6PoolEc2Id"]
    """<p>The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.</p>"""
    ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block from the IPv6 address pool. You must also specify <code>Ipv6Pool</code> in the request.</p> <p>To let Amazon choose the IPv6 CIDR block for you, omit this parameter.</p>"""
    ipv4_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>. </p>"""
    ipv4_netmask_length: NotRequired["aws_sdk_ec2.types.netmask_length.NetmaskLength"]
    """<p>The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv6_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of an IPv6 IPAM pool which will be used to allocate this VPC an IPv6 CIDR. IPAM is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across Amazon Web Services Regions and accounts throughout your Amazon Web Services Organization. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv6_netmask_length: NotRequired["aws_sdk_ec2.types.netmask_length.NetmaskLength"]
    """<p>The netmask length of the IPv6 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html\">What is IPAM?</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
    ipv6_cidr_block_network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the address to this location.</p> <p> You must set <code>AmazonProvidedIpv6CidrBlock</code> to <code>true</code> to use this parameter.</p>"""
    vpc_encryption_control: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_configuration.VpcEncryptionControlConfiguration"
    ]
    """<p>Specifies the encryption control configuration to apply to the VPC during creation. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirements.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html\">Enforce VPC encryption in transit</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the VPC.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy options for instances launched into the VPC. For <code>default</code>, instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For <code>dedicated</code>, instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of <code>dedicated</code> or <code>host</code> into a dedicated tenancy VPC. </p> <p> <b>Important:</b> The <code>host</code> value cannot be used with this parameter. Use the <code>default</code> or <code>dedicated</code> values only.</p> <p>Default: <code>default</code> </p>"""
    amazon_provided_ipv6_cidr_block: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block.</p>"""
