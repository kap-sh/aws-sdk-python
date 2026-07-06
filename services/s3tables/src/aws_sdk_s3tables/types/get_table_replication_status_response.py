"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableReplicationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.replication_destination_statuses
    import aws_sdk_s3tables.types.table_arn


class GetTableReplicationStatusResponse(TypedDict, closed=True):
    source_table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the source table being replicated.</p>"""
    destinations: "aws_sdk_s3tables.types.replication_destination_statuses.ReplicationDestinationStatuses"
    """<p>An array of status information for each replication destination, including the current state, last successful update, and any error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableReplicationStatusResponse) -> dict:
    out: dict = {}
    out["sourceTableArn"] = value["source_table_arn"]
    import aws_sdk_s3tables.types.replication_destination_statuses

    out["destinations"] = (
        aws_sdk_s3tables.types.replication_destination_statuses.serialize_json(
            value["destinations"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTableReplicationStatusResponse:
    out: GetTableReplicationStatusResponse = {}  # type: ignore[typeddict-item]
    if "sourceTableArn" in data:
        out["source_table_arn"] = data["sourceTableArn"]
    else:
        raise DeserializationError(
            "GetTableReplicationStatusResponse.source_table_arn required"
        )
    if "destinations" in data:
        import aws_sdk_s3tables.types.replication_destination_statuses

        out["destinations"] = (
            aws_sdk_s3tables.types.replication_destination_statuses.deserialize_json(
                data["destinations"]
            )
        )
    else:
        raise DeserializationError(
            "GetTableReplicationStatusResponse.destinations required"
        )
    return out
