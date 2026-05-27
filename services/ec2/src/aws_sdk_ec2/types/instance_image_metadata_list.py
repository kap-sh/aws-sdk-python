"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceImageMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_image_metadata

InstanceImageMetadataList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_image_metadata.InstanceImageMetadata"
]
