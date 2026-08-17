"""Generated from Smithy shape ``com.amazonaws.dynamodb#KinesisDataStreamDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.approximate_creation_date_time_precision
    import capo_dynamodb.types.destination_status
    import capo_dynamodb.types.stream_arn
    import capo_dynamodb.types.string


class KinesisDataStreamDestination(TypedDict, closed=True):
    stream_arn: NotRequired["capo_dynamodb.types.stream_arn.StreamArn"]
    """<p>The ARN for a specific Kinesis data stream.</p>"""
    destination_status: NotRequired[
        "capo_dynamodb.types.destination_status.DestinationStatus"
    ]
    """<p>The current status of replication.</p>"""
    destination_status_description: NotRequired["capo_dynamodb.types.string.String"]
    """<p>The human-readable string that corresponds to the replica status.</p>"""
    approximate_creation_date_time_precision: NotRequired[
        "capo_dynamodb.types.approximate_creation_date_time_precision.ApproximateCreationDateTimePrecision"
    ]
    """<p>The precision of the Kinesis data stream timestamp. The values are either <code>MILLISECOND</code> or <code>MICROSECOND</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KinesisDataStreamDestination) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    if "destination_status" in value:
        import capo_dynamodb.types.destination_status

        out["DestinationStatus"] = (
            capo_dynamodb.types.destination_status.serialize_aws_json_1_0(
                value["destination_status"]
            )
        )
    if "destination_status_description" in value:
        out["DestinationStatusDescription"] = value["destination_status_description"]
    if "approximate_creation_date_time_precision" in value:
        import capo_dynamodb.types.approximate_creation_date_time_precision

        out["ApproximateCreationDateTimePrecision"] = (
            capo_dynamodb.types.approximate_creation_date_time_precision.serialize_aws_json_1_0(
                value["approximate_creation_date_time_precision"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> KinesisDataStreamDestination:
    out: KinesisDataStreamDestination = {}  # type: ignore[typeddict-item]
    if data.get("StreamArn") is not None:
        out["stream_arn"] = data["StreamArn"]
    if data.get("DestinationStatus") is not None:
        import capo_dynamodb.types.destination_status

        out["destination_status"] = (
            capo_dynamodb.types.destination_status.deserialize_aws_json_1_0(
                data["DestinationStatus"]
            )
        )
    if data.get("DestinationStatusDescription") is not None:
        out["destination_status_description"] = data["DestinationStatusDescription"]
    if data.get("ApproximateCreationDateTimePrecision") is not None:
        import capo_dynamodb.types.approximate_creation_date_time_precision

        out["approximate_creation_date_time_precision"] = (
            capo_dynamodb.types.approximate_creation_date_time_precision.deserialize_aws_json_1_0(
                data["ApproximateCreationDateTimePrecision"]
            )
        )
    return out
