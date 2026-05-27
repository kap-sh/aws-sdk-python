"""Generated from Smithy shape ``com.amazonaws.ec2#TagSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.tag_specification

TagSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.tag_specification.TagSpecification"
]
