"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplatePrivateDnsNameOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.hostname_type


class LaunchTemplatePrivateDnsNameOptions(TypedDict):
    hostname_type: NotRequired["aws_sdk_ec2.types.hostname_type.HostnameType"]
    """<p>The type of hostname to assign to an instance.</p>"""
    enable_resource_name_dns_a_record: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS A records.</p>"""
    enable_resource_name_dns_aaaa_record: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether to respond to DNS queries for instance hostnames with DNS AAAA records.</p>"""
