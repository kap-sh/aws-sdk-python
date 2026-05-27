"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_acl_entry

NetworkAclEntryList: TypeAlias = list[
    "aws_sdk_ec2.types.network_acl_entry.NetworkAclEntry"
]
