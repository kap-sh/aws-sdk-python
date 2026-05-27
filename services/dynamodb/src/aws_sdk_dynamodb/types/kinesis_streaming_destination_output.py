"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisStreamingDestinationOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.destination_status
    import aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.table_name


class KinesisStreamingDestinationOutput(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The name of the table being modified.</p>"""
    stream_arn: NotRequired["aws_sdk_dynamodb.types.stream_arn.StreamArn"]
    """<p>The ARN for the specific Kinesis data stream.</p>"""
    destination_status: NotRequired[
        "aws_sdk_dynamodb.types.destination_status.DestinationStatus"
    ]
    """<p>The current status of the replication.</p>"""
    enable_kinesis_streaming_configuration: NotRequired[
        "aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration.EnableKinesisStreamingConfiguration"
    ]
    """<p>The destination for the Kinesis streaming information that is being enabled.</p>"""
