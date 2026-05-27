"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_details_list
    import aws_sdk_ec2.types.summary_status


class InstanceStatusSummary(TypedDict):
    details: NotRequired[
        "aws_sdk_ec2.types.instance_status_details_list.InstanceStatusDetailsList"
    ]
    """<p>The system instance health or application instance health.</p>"""
    status: NotRequired["aws_sdk_ec2.types.summary_status.SummaryStatus"]
    """<p>The status.</p>"""
