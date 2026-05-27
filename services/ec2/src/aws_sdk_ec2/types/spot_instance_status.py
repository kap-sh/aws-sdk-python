"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string


class SpotInstanceStatus(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status code. For a list of status codes, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html#spot-instance-request-status-understand\">Spot request status codes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description for the status code.</p>"""
    update_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time of the most recent status update, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
