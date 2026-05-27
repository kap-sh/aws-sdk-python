"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceConnectEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_connect_endpoint_id
    import aws_sdk_ec2.types.ip_address_type
    import aws_sdk_ec2.types.security_group_id_string_list_request


class ModifyInstanceConnectEndpointRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_connect_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_id.InstanceConnectEndpointId"
    ]
    """<p>The ID of the EC2 Instance Connect Endpoint to modify.</p>"""
    ip_address_type: NotRequired["aws_sdk_ec2.types.ip_address_type.IpAddressType"]
    """<p>The new IP address type for the EC2 Instance Connect Endpoint.</p> <note> <p> <code>PreserveClientIp</code> is only supported on IPv4 EC2 Instance Connect Endpoints. To use <code>PreserveClientIp</code>, the value for <code>IpAddressType</code> must be <code>ipv4</code>.</p> </note>"""
    security_group_ids: NotRequired[
        "aws_sdk_ec2.types.security_group_id_string_list_request.SecurityGroupIdStringListRequest"
    ]
    """<p>Changes the security groups for the EC2 Instance Connect Endpoint. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.</p>"""
    preserve_client_ip: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the client IP address is preserved as the source when you connect to a resource. The following are the possible values.</p> <ul> <li> <p> <code>true</code> - Use the IP address of the client. Your instance must have an IPv4 address.</p> </li> <li> <p> <code>false</code> - Use the IP address of the network interface.</p> </li> </ul>"""
