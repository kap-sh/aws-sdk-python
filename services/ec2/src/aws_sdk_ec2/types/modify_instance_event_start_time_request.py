"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceEventStartTimeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.string


class ModifyInstanceEventStartTimeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance with the scheduled event.</p>"""
    instance_event_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the event whose date and time you are modifying.</p>"""
    not_before: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The new date and time when the event will take place.</p>"""
