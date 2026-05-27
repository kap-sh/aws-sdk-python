"""Generated from Smithy shape ``com.amazonaws.ec2#ImageProviderRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_provider_request

ImageProviderRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.image_provider_request.ImageProviderRequest"
]
