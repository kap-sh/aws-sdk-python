"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyPrivateDnsNameOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.hostname_type
    import aws_sdk_ec2.types.instance_id


class ModifyPrivateDnsNameOptionsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    private_dns_hostname_type: NotRequired[
        "aws_sdk_ec2.types.hostname_type.HostnameType"
    ]
    """<p>The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 only subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID.</p>"""
    enable_resource_name_dns_a_record: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS A records.</p>"""
    enable_resource_name_dns_aaaa_record: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.</p>"""
