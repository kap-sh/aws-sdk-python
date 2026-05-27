"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerMonitoredTagKeysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list


class UpdateCapacityManagerMonitoredTagKeysResult(TypedDict):
    capacity_manager_tag_keys: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_monitored_tag_key_list.CapacityManagerMonitoredTagKeyList"
    ]
    """<p> The list of tag keys affected by the update, including their current status and metadata. </p>"""
