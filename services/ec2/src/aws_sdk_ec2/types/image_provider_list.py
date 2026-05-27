"""Generated from Smithy shape ``com.amazonaws.ec2#ImageProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_provider

ImageProviderList: TypeAlias = list["aws_sdk_ec2.types.image_provider.ImageProvider"]
