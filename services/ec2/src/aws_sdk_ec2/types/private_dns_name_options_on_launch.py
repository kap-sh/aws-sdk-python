"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsNameOptionsOnLaunch``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.hostname_type


class PrivateDnsNameOptionsOnLaunch(TypedDict):
    hostname_type: NotRequired["aws_sdk_ec2.types.hostname_type.HostnameType"]
    """<p>The type of hostname for EC2 instances. For IPv4 only subnets, an instance DNS name must be based on the instance IPv4 address. For IPv6 only subnets, an instance DNS name must be based on the instance ID. For dual-stack subnets, you can specify whether DNS names use the instance IPv4 address or the instance ID.</p>"""
    enable_resource_name_dns_a_record: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS A records.</p>"""
    enable_resource_name_dns_aaaa_record: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether to respond to DNS queries for instance hostname with DNS AAAA records.</p>"""
