"""Generated from Smithy shape ``com.amazonaws.ec2#ManagedPrefixListSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_prefix_list

ManagedPrefixListSet: TypeAlias = list[
    "aws_sdk_ec2.types.managed_prefix_list.ManagedPrefixList"
]
