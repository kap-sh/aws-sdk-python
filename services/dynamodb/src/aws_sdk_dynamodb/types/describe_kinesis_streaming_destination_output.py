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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeKinesisStreamingDestinationOutput) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "kinesis_data_stream_destinations" in value:
        import aws_sdk_dynamodb.types.kinesis_data_stream_destinations

        out["KinesisDataStreamDestinations"] = (
            aws_sdk_dynamodb.types.kinesis_data_stream_destinations.serialize_aws_json_1_0(
                value["kinesis_data_stream_destinations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeKinesisStreamingDestinationOutput:
    out: DescribeKinesisStreamingDestinationOutput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "KinesisDataStreamDestinations" in data:
        import aws_sdk_dynamodb.types.kinesis_data_stream_destinations

        out["kinesis_data_stream_destinations"] = (
            aws_sdk_dynamodb.types.kinesis_data_stream_destinations.deserialize_aws_json_1_0(
                data["KinesisDataStreamDestinations"]
            )
        )
    return out
