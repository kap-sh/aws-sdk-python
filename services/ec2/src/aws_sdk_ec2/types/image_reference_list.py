"""Generated from Smithy shape ``com.amazonaws.ec2#ImageReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_reference

ImageReferenceList: TypeAlias = list["aws_sdk_ec2.types.image_reference.ImageReference"]
