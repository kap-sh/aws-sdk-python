"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateKinesisStreamingDestinationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.update_kinesis_streaming_configuration


class UpdateKinesisStreamingDestinationInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The table name for the Kinesis streaming destination input. You can also provide the ARN of the table in this parameter.</p>"""
    stream_arn: "aws_sdk_dynamodb.types.stream_arn.StreamArn"
    """<p>The Amazon Resource Name (ARN) for the Kinesis stream input.</p>"""
    update_kinesis_streaming_configuration: NotRequired[
        "aws_sdk_dynamodb.types.update_kinesis_streaming_configuration.UpdateKinesisStreamingConfiguration"
    ]
    """<p>The command to update the Kinesis stream configuration.</p>"""
