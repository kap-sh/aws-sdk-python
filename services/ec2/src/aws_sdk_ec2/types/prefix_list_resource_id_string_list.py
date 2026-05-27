"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListResourceIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.prefix_list_resource_id

PrefixListResourceIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
]
