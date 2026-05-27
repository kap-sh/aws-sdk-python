"""Generated from Smithy shape ``com.amazonaws.ec2#GroupBySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.group_by

GroupBySet: TypeAlias = list["aws_sdk_ec2.types.group_by.GroupBy"]
