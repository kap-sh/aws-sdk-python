"""Generated from Smithy shape ``com.amazonaws.ec2#ImageRecycleBinInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class ImageRecycleBinInfo(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the AMI.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the AMI.</p>"""
    recycle_bin_enter_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the AMI entered the Recycle Bin.</p>"""
    recycle_bin_exit_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the AMI is to be permanently deleted from the Recycle Bin.</p>"""
