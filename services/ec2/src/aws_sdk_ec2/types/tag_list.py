"""Generated from Smithy shape ``com.amazonaws.ec2#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.tag

TagList: TypeAlias = list["aws_sdk_ec2.types.tag.Tag"]
