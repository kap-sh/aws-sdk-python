"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisStreamingDestinationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KinesisStreamingDestinationInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["StreamArn"] = value["stream_arn"]
    if "enable_kinesis_streaming_configuration" in value:
        import aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration

        out["EnableKinesisStreamingConfiguration"] = (
            aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration.serialize_aws_json_1_0(
                value["enable_kinesis_streaming_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KinesisStreamingDestinationInput:
    out: KinesisStreamingDestinationInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "KinesisStreamingDestinationInput.table_name required"
        )
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    else:
        raise DeserializationError(
            "KinesisStreamingDestinationInput.stream_arn required"
        )
    if "EnableKinesisStreamingConfiguration" in data:
        import aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration

        out["enable_kinesis_streaming_configuration"] = (
            aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration.deserialize_aws_json_1_0(
                data["EnableKinesisStreamingConfiguration"]
            )
        )
    return out
