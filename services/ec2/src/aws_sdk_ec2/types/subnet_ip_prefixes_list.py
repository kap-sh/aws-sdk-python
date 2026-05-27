"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpPrefixesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_ip_prefixes

SubnetIpPrefixesList: TypeAlias = list[
    "aws_sdk_ec2.types.subnet_ip_prefixes.SubnetIpPrefixes"
]
