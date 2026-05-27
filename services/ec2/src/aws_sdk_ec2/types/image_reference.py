"""Generated from Smithy shape ``com.amazonaws.ec2#ImageReference``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_reference_resource_type
    import aws_sdk_ec2.types.string


class ImageReference(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the referenced image.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.image_reference_resource_type.ImageReferenceResourceType"
    ]
    """<p>The type of resource referencing the image.</p>"""
    arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource referencing the image.</p>"""
