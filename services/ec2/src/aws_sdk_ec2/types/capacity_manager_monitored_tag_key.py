"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerMonitoredTagKey``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_status
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class CapacityManagerMonitoredTagKey(TypedDict):
    tag_key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The tag key being monitored. </p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_monitored_tag_key_status.CapacityManagerMonitoredTagKeyStatus"
    ]
    """<p> The current status of the monitored tag key. Valid values are <code>activating</code>, <code>activated</code>, <code>deactivating</code>, and <code>suspended</code>. </p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> A message providing additional details about the current status of the monitored tag key. </p>"""
    capacity_manager_provided: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Indicates whether this tag key is provided by Capacity Manager by default, rather than being user-activated. </p>"""
    earliest_datapoint_timestamp: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The earliest timestamp from which tag data is available for queries, in UTC ISO 8601 format. </p>"""
