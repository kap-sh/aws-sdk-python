"""Generated from Smithy shape ``com.amazonaws.ec2#ClientData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.string


class ClientData(TypedDict):
    comment: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A user-defined comment about the disk upload.</p>"""
    upload_end: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that the disk upload ends.</p>"""
    upload_size: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The size of the uploaded disk image, in GiB.</p>"""
    upload_start: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that the disk upload starts.</p>"""
