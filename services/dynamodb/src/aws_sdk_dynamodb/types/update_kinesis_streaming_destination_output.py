"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateKinesisStreamingDestinationOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.destination_status
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.table_name
    import aws_sdk_dynamodb.types.update_kinesis_streaming_configuration


class UpdateKinesisStreamingDestinationOutput(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The table name for the Kinesis streaming destination output.</p>"""
    stream_arn: NotRequired["aws_sdk_dynamodb.types.stream_arn.StreamArn"]
    """<p>The ARN for the Kinesis stream input.</p>"""
    destination_status: NotRequired[
        "aws_sdk_dynamodb.types.destination_status.DestinationStatus"
    ]
    """<p>The status of the attempt to update the Kinesis streaming destination output.</p>"""
    update_kinesis_streaming_configuration: NotRequired[
        "aws_sdk_dynamodb.types.update_kinesis_streaming_configuration.UpdateKinesisStreamingConfiguration"
    ]
    """<p>The command to update the Kinesis streaming destination configuration.</p>"""
