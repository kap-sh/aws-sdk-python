"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageResourceTypeRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_usage_resource_type_request

ImageUsageResourceTypeRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.image_usage_resource_type_request.ImageUsageResourceTypeRequest"
]
