"""Generated from Smithy shape ``com.amazonaws.ec2#TagDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.tag_description

TagDescriptionList: TypeAlias = list["aws_sdk_ec2.types.tag_description.TagDescription"]
