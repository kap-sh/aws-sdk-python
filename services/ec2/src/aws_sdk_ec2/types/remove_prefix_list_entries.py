"""Generated from Smithy shape ``com.amazonaws.ec2#RemovePrefixListEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.remove_prefix_list_entry

RemovePrefixListEntries: TypeAlias = list[
    "aws_sdk_ec2.types.remove_prefix_list_entry.RemovePrefixListEntry"
]
