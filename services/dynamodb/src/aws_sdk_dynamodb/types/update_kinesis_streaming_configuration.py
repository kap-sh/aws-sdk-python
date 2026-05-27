"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateKinesisStreamingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.approximate_creation_date_time_precision


class UpdateKinesisStreamingConfiguration(TypedDict):
    approximate_creation_date_time_precision: NotRequired[
        "aws_sdk_dynamodb.types.approximate_creation_date_time_precision.ApproximateCreationDateTimePrecision"
    ]
    """<p>Enables updating the precision of Kinesis data stream timestamp. </p>"""
