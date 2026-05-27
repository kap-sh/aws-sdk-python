"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateTimeToLiveOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.time_to_live_specification


class UpdateTimeToLiveOutput(TypedDict):
    time_to_live_specification: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_specification.TimeToLiveSpecification"
    ]
    """<p>Represents the output of an <code>UpdateTimeToLive</code> operation.</p>"""
