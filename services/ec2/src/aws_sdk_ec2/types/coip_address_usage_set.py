"""Generated from Smithy shape ``com.amazonaws.ec2#CoipAddressUsageSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_address_usage

CoipAddressUsageSet: TypeAlias = list[
    "aws_sdk_ec2.types.coip_address_usage.CoipAddressUsage"
]
