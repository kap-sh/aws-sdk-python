"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisStreamingDestinationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.destination_status
    import aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.table_name


class KinesisStreamingDestinationOutput(TypedDict, closed=True):
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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KinesisStreamingDestinationOutput) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    if "destination_status" in value:
        import aws_sdk_dynamodb.types.destination_status

        out["DestinationStatus"] = (
            aws_sdk_dynamodb.types.destination_status.serialize_aws_json_1_0(
                value["destination_status"]
            )
        )
    if "enable_kinesis_streaming_configuration" in value:
        import aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration

        out["EnableKinesisStreamingConfiguration"] = (
            aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration.serialize_aws_json_1_0(
                value["enable_kinesis_streaming_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KinesisStreamingDestinationOutput:
    out: KinesisStreamingDestinationOutput = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    if "DestinationStatus" in data:
        import aws_sdk_dynamodb.types.destination_status

        out["destination_status"] = (
            aws_sdk_dynamodb.types.destination_status.deserialize_aws_json_1_0(
                data["DestinationStatus"]
            )
        )
    if "EnableKinesisStreamingConfiguration" in data:
        import aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration

        out["enable_kinesis_streaming_configuration"] = (
            aws_sdk_dynamodb.types.enable_kinesis_streaming_configuration.deserialize_aws_json_1_0(
                data["EnableKinesisStreamingConfiguration"]
            )
        )
    return out
