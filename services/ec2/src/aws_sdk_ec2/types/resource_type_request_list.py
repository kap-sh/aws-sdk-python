"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_type_request

ResourceTypeRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.resource_type_request.ResourceTypeRequest"
]
