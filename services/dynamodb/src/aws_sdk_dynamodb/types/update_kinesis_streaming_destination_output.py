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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateKinesisStreamingDestinationOutput) -> dict:
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
    if "update_kinesis_streaming_configuration" in value:
        import aws_sdk_dynamodb.types.update_kinesis_streaming_configuration

        out["UpdateKinesisStreamingConfiguration"] = (
            aws_sdk_dynamodb.types.update_kinesis_streaming_configuration.serialize_aws_json_1_0(
                value["update_kinesis_streaming_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateKinesisStreamingDestinationOutput:
    out: UpdateKinesisStreamingDestinationOutput = {}  # type: ignore[typeddict-item]
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
    if "UpdateKinesisStreamingConfiguration" in data:
        import aws_sdk_dynamodb.types.update_kinesis_streaming_configuration

        out["update_kinesis_streaming_configuration"] = (
            aws_sdk_dynamodb.types.update_kinesis_streaming_configuration.deserialize_aws_json_1_0(
                data["UpdateKinesisStreamingConfiguration"]
            )
        )
    return out
