"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeKinesisStreamingDestinationOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.kinesis_data_stream_destinations
    import aws_sdk_dynamodb.types.table_name


class DescribeKinesisStreamingDestinationOutput(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The name of the table being described.</p>"""
    kinesis_data_stream_destinations: NotRequired[
        "aws_sdk_dynamodb.types.kinesis_data_stream_destinations.KinesisDataStreamDestinations"
    ]
    """<p>The list of replica structures for the table being described.</p>"""
