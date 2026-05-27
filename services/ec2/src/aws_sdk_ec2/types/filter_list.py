"""Generated from Smithy shape ``com.amazonaws.ec2#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.filter

FilterList: TypeAlias = list["aws_sdk_ec2.types.filter.Filter"]
