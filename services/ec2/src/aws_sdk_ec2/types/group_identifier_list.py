"""Generated from Smithy shape ``com.amazonaws.ec2#GroupIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.group_identifier

GroupIdentifierList: TypeAlias = list[
    "aws_sdk_ec2.types.group_identifier.GroupIdentifier"
]
