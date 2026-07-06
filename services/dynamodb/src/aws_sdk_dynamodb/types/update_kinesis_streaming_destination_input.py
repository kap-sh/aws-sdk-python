"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateKinesisStreamingDestinationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.update_kinesis_streaming_configuration


class UpdateKinesisStreamingDestinationInput(TypedDict, closed=True):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The table name for the Kinesis streaming destination input. You can also provide the ARN of the table in this parameter.</p>"""
    stream_arn: "aws_sdk_dynamodb.types.stream_arn.StreamArn"
    """<p>The Amazon Resource Name (ARN) for the Kinesis stream input.</p>"""
    update_kinesis_streaming_configuration: NotRequired[
        "aws_sdk_dynamodb.types.update_kinesis_streaming_configuration.UpdateKinesisStreamingConfiguration"
    ]
    """<p>The command to update the Kinesis stream configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateKinesisStreamingDestinationInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    out["StreamArn"] = value["stream_arn"]
    if "update_kinesis_streaming_configuration" in value:
        import aws_sdk_dynamodb.types.update_kinesis_streaming_configuration

        out["UpdateKinesisStreamingConfiguration"] = (
            aws_sdk_dynamodb.types.update_kinesis_streaming_configuration.serialize_aws_json_1_0(
                value["update_kinesis_streaming_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateKinesisStreamingDestinationInput:
    out: UpdateKinesisStreamingDestinationInput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "UpdateKinesisStreamingDestinationInput.table_name required"
        )
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    else:
        raise DeserializationError(
            "UpdateKinesisStreamingDestinationInput.stream_arn required"
        )
    if "UpdateKinesisStreamingConfiguration" in data:
        import aws_sdk_dynamodb.types.update_kinesis_streaming_configuration

        out["update_kinesis_streaming_configuration"] = (
            aws_sdk_dynamodb.types.update_kinesis_streaming_configuration.deserialize_aws_json_1_0(
                data["UpdateKinesisStreamingConfiguration"]
            )
        )
    return out
