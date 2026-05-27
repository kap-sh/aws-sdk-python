"""Generated from Smithy shape ``com.amazonaws.ec2#ImageAncestryEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class ImageAncestryEntry(TypedDict):
    creation_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when this AMI was created.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of this AMI.</p>"""
    image_owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The owner alias (<code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code> ) of this AMI, if one is assigned. Otherwise, the value is <code>null</code>.</p>"""
    source_image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the parent AMI.</p>"""
    source_image_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the parent AMI.</p>"""
