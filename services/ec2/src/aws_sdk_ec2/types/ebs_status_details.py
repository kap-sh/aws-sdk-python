"""Generated from Smithy shape ``com.amazonaws.ec2#EbsStatusDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.status_name
    import aws_sdk_ec2.types.status_type


class EbsStatusDetails(TypedDict):
    impaired_since: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the attached EBS status check failed.</p>"""
    name: NotRequired["aws_sdk_ec2.types.status_name.StatusName"]
    """<p>The name of the attached EBS status check.</p>"""
    status: NotRequired["aws_sdk_ec2.types.status_type.StatusType"]
    """<p>The result of the attached EBS status check.</p>"""
