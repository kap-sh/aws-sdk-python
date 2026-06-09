"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisDataStreamDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.approximate_creation_date_time_precision
    import aws_sdk_dynamodb.types.destination_status
    import aws_sdk_dynamodb.types.stream_arn
    import aws_sdk_dynamodb.types.string


class KinesisDataStreamDestination(TypedDict):
    stream_arn: NotRequired["aws_sdk_dynamodb.types.stream_arn.StreamArn"]
    """<p>The ARN for a specific Kinesis data stream.</p>"""
    destination_status: NotRequired[
        "aws_sdk_dynamodb.types.destination_status.DestinationStatus"
    ]
    """<p>The current status of replication.</p>"""
    destination_status_description: NotRequired["aws_sdk_dynamodb.types.string.String"]
    """<p>The human-readable string that corresponds to the replica status.</p>"""
    approximate_creation_date_time_precision: NotRequired[
        "aws_sdk_dynamodb.types.approximate_creation_date_time_precision.ApproximateCreationDateTimePrecision"
    ]
    """<p>The precision of the Kinesis data stream timestamp. The values are either <code>MILLISECOND</code> or <code>MICROSECOND</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KinesisDataStreamDestination) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    if "destination_status" in value:
        import aws_sdk_dynamodb.types.destination_status

        out["DestinationStatus"] = (
            aws_sdk_dynamodb.types.destination_status.serialize_aws_json_1_0(
                value["destination_status"]
            )
        )
    if "destination_status_description" in value:
        out["DestinationStatusDescription"] = value["destination_status_description"]
    if "approximate_creation_date_time_precision" in value:
        import aws_sdk_dynamodb.types.approximate_creation_date_time_precision

        out["ApproximateCreationDateTimePrecision"] = (
            aws_sdk_dynamodb.types.approximate_creation_date_time_precision.serialize_aws_json_1_0(
                value["approximate_creation_date_time_precision"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KinesisDataStreamDestination:
    out: KinesisDataStreamDestination = {}  # type: ignore[typeddict-item]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    if "DestinationStatus" in data:
        import aws_sdk_dynamodb.types.destination_status

        out["destination_status"] = (
            aws_sdk_dynamodb.types.destination_status.deserialize_aws_json_1_0(
                data["DestinationStatus"]
            )
        )
    if "DestinationStatusDescription" in data:
        out["destination_status_description"] = data["DestinationStatusDescription"]
    if "ApproximateCreationDateTimePrecision" in data:
        import aws_sdk_dynamodb.types.approximate_creation_date_time_precision

        out["approximate_creation_date_time_precision"] = (
            aws_sdk_dynamodb.types.approximate_creation_date_time_precision.deserialize_aws_json_1_0(
                data["ApproximateCreationDateTimePrecision"]
            )
        )
    return out
