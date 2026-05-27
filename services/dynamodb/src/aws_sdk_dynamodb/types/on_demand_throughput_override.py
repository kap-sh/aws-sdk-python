"""Generated from Smithy shape ``com.amazonaws.dynamodb#OnDemandThroughputOverride``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.long_object


class OnDemandThroughputOverride(TypedDict):
    max_read_request_units: NotRequired["aws_sdk_dynamodb.types.long_object.LongObject"]
    """<p>Maximum number of read request units for the specified replica table.</p>"""
