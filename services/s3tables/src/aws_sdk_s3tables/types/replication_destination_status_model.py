"""Generated from Smithy shape ``com.amazonaws.s3tables#ReplicationDestinationStatusModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.last_successful_replicated_update
    import aws_sdk_s3tables.types.replication_status
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.table_bucket_arn


class ReplicationDestinationStatusModel(TypedDict, closed=True):
    replication_status: "aws_sdk_s3tables.types.replication_status.ReplicationStatus"
    """<p>The current status of replication to this destination.</p>"""
    destination_table_bucket_arn: (
        "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    )
    """<p>The Amazon Resource Name (ARN) of the destination table bucket.</p>"""
    destination_table_arn: NotRequired["aws_sdk_s3tables.types.table_arn.TableARN"]
    """<p>The Amazon Resource Name (ARN) of the destination table.</p>"""
    last_successful_replicated_update: NotRequired[
        "aws_sdk_s3tables.types.last_successful_replicated_update.LastSuccessfulReplicatedUpdate"
    ]
    """<p>Information about the most recent successful replication update to this destination.</p>"""
    failure_message: NotRequired["str"]
    """<p>If replication has failed, this field contains an error message describing the failure reason.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationDestinationStatusModel) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.replication_status

    out["replicationStatus"] = aws_sdk_s3tables.types.replication_status.serialize_json(
        value["replication_status"]
    )
    out["destinationTableBucketArn"] = value["destination_table_bucket_arn"]
    if "destination_table_arn" in value:
        out["destinationTableArn"] = value["destination_table_arn"]
    if "last_successful_replicated_update" in value:
        import aws_sdk_s3tables.types.last_successful_replicated_update

        out["lastSuccessfulReplicatedUpdate"] = (
            aws_sdk_s3tables.types.last_successful_replicated_update.serialize_json(
                value["last_successful_replicated_update"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_json(data: dict) -> ReplicationDestinationStatusModel:
    out: ReplicationDestinationStatusModel = {}  # type: ignore[typeddict-item]
    if "replicationStatus" in data:
        import aws_sdk_s3tables.types.replication_status

        out["replication_status"] = (
            aws_sdk_s3tables.types.replication_status.deserialize_json(
                data["replicationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "ReplicationDestinationStatusModel.replication_status required"
        )
    if "destinationTableBucketArn" in data:
        out["destination_table_bucket_arn"] = data["destinationTableBucketArn"]
    else:
        raise DeserializationError(
            "ReplicationDestinationStatusModel.destination_table_bucket_arn required"
        )
    if "destinationTableArn" in data:
        out["destination_table_arn"] = data["destinationTableArn"]
    if "lastSuccessfulReplicatedUpdate" in data:
        import aws_sdk_s3tables.types.last_successful_replicated_update

        out["last_successful_replicated_update"] = (
            aws_sdk_s3tables.types.last_successful_replicated_update.deserialize_json(
                data["lastSuccessfulReplicatedUpdate"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
