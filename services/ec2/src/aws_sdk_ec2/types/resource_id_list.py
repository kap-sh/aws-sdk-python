"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.taggable_resource_id

ResourceIdList: TypeAlias = list[
    "aws_sdk_ec2.types.taggable_resource_id.TaggableResourceId"
]
