"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisDataStreamDestination``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.approximate_creation_date_time_precision
    import aws_sdk_dynamodb.types.destination_status
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.string


class KinesisDataStreamDestination(TypedDict):
    stream_arn: NotRequired["aws_sdk_dynamodb.types.stream_arn.StreamArn"]
    """<p>The ARN for a specific Kinesis data stream.</p>"""
    destination_status: NotRequired[
        "aws_sdk_dynamodb.types.destination_status.DestinationStatus"
    ]
    """<p>The current status of replication.</p>"""
    destination_status_description: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p>The human-readable string that corresponds to the replica status.</p>"""
    approximate_creation_date_time_precision: NotRequired[
        "aws_sdk_dynamodb.types.approximate_creation_date_time_precision.ApproximateCreationDateTimePrecision"
    ]
    """<p>The precision of the Kinesis data stream timestamp. The values are either <code>MILLISECOND</code> or <code>MICROSECOND</code>.</p>"""
