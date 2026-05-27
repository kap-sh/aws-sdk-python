"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisStreamingDestinationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.table_arn


class KinesisStreamingDestinationInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the DynamoDB table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    stream_arn: "aws_sdk_dynamodb.types.stream_arn.StreamArn"
    """<p>The ARN for a Kinesis data stream.</p>"""
    enable_kinesis_streaming_configuration: NotRequired[
        "aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration.EnableKinesisStreamingConfiguration"
    ]
    """<p>The source for the Kinesis streaming information that is being enabled.</p>"""
