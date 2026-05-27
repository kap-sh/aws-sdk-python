"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMonitoredTagKeysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list
    import aws_sdk_ec2.types.string


class GetCapacityManagerMonitoredTagKeysResult(TypedDict):
    capacity_manager_tag_keys: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list.CapacityManagerMonitoredTagKeyList"
    ]
    """<p> The list of tag keys being monitored by Capacity Manager, including their current status and metadata. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""
