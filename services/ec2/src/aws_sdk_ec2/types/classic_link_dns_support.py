"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLinkDnsSupport``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ClassicLinkDnsSupport(TypedDict):
    classic_link_dns_supported: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether ClassicLink DNS support is enabled for the VPC.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
