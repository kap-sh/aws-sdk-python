"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceConnectEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.security_group_id_string_list_request
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_specification_list


class CreateInstanceConnectEndpointRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which to create the EC2 Instance Connect Endpoint.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list_request.SecurityGroupIdStringListRequest"
    ]
    """<p>One or more security groups to associate with the endpoint. If you don't specify a security group, the default security group for your VPC will be associated with the endpoint.</p>"""
    preserve_client_ip: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the client IP address is preserved as the source. The following are the possible values.</p> <ul> <li> <p> <code>true</code> - Use the client IP address as the source.</p> </li> <li> <p> <code>false</code> - Use the network interface IP address as the source.</p> </li> </ul> <note> <p> <code>PreserveClientIp</code> is only supported on IPv4 EC2 Instance Connect Endpoints. To use <code>PreserveClientIp</code>, the value for <code>IpAddressType</code> must be <code>ipv4</code>.</p> </note> <p>Default: <code>false</code> </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the EC2 Instance Connect Endpoint during creation.</p>"""
    ip_address_type: NotRequired["aws_sdk_ec2.types.ip_address_type.IpAddressType"]
    """<p>The IP address type of the endpoint.</p> <p>If no value is specified, the default value is determined by the IP address type of the subnet:</p> <ul> <li> <p> <code>dualstack</code> - If the subnet has both IPv4 and IPv6 CIDRs</p> </li> <li> <p> <code>ipv4</code> - If the subnet has only IPv4 CIDRs</p> </li> <li> <p> <code>ipv6</code> - If the subnet has only IPv6 CIDRs</p> </li> </ul> <note> <p> <code>PreserveClientIp</code> is only supported on IPv4 EC2 Instance Connect Endpoints. To use <code>PreserveClientIp</code>, the value for <code>IpAddressType</code> must be <code>ipv4</code>.</p> </note>"""
