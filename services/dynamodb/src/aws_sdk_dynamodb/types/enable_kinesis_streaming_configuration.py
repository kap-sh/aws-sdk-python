"""Generated from Smithy shape ``com.amazonaws.dynamodb#EnableKinesisStreamingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.approximate_creation_date_time_precision


class EnableKinesisStreamingConfiguration(TypedDict):
    approximate_creation_date_time_precision: NotRequired[
        "aws_sdk_dynamodb.types.approximate_creation_date_time_precision.ApproximateCreationDateTimePrecision"
    ]
    """<p>Toggle for the precision of Kinesis data stream timestamp. The values are either <code>MILLISECOND</code> or <code>MICROSECOND</code>.</p>"""
