"""Generated from Smithy shape ``com.amazonaws.ec2#AddPrefixListEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_prefix_list_entry

AddPrefixListEntries: TypeAlias = list[
    "aws_sdk_ec2.types.add_prefix_list_entry.AddPrefixListEntry"
]
