"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLinkDnsSupportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_link_dns_support

ClassicLinkDnsSupportList: TypeAlias = list[
    "aws_sdk_ec2.types.classic_link_dns_support.ClassicLinkDnsSupport"
]
