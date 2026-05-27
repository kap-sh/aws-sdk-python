"""Generated from Smithy shape ``com.amazonaws.ec2#EbsStatusSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_status_details_list
    import aws_sdk_ec2.types.summary_status


class EbsStatusSummary(TypedDict):
    details: NotRequired[
        "aws_sdk_ec2.types.ebs_status_details_list.EbsStatusDetailsList"
    ]
    """<p>Details about the attached EBS status check for an instance.</p>"""
    status: NotRequired["aws_sdk_ec2.types.summary_status.SummaryStatus"]
    """<p>The current status.</p>"""
