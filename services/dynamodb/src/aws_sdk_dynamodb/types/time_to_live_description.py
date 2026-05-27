"""Generated from Smithy shape ``com.amazonaws.dynamodb#TimeToLiveDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.time_to_live_attribute_name
    import aws_sdk_dynamodb.types.time_to_live_status


class TimeToLiveDescription(TypedDict):
    time_to_live_status: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_status.TimeToLiveStatus"
    ]
    """<p> The TTL status for the table.</p>"""
    attribute_name: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_attribute_name.TimeToLiveAttributeName"
    ]
    """<p> The name of the TTL attribute for items in the table.</p>"""
