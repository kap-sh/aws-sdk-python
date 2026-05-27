"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeTimeToLiveOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.time_to_live_description


class DescribeTimeToLiveOutput(TypedDict):
    time_to_live_description: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_description.TimeToLiveDescription"
    ]
    """<p></p>"""
