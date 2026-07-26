"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseSnapshotInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.database_table_name
    import capo_firehose.types.failure_description
    import capo_firehose.types.non_empty_string_without_whitespace
    import capo_firehose.types.snapshot_requested_by
    import capo_firehose.types.snapshot_status
    import capo_firehose.types.timestamp


class DatabaseSnapshotInfo(TypedDict, closed=True):
    id: "capo_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    """<p> The identifier of the current snapshot of the table in source database endpoint. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    table: "capo_firehose.types.database_table_name.DatabaseTableName"
    """<p> The fully qualified name of the table in source database endpoint that Firehose reads. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    request_timestamp: "capo_firehose.types.timestamp.Timestamp"
    """<p> The timestamp when the current snapshot is taken on the table. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    requested_by: "capo_firehose.types.snapshot_requested_by.SnapshotRequestedBy"
    """<p> The principal that sent the request to take the current snapshot on the table. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    status: "capo_firehose.types.snapshot_status.SnapshotStatus"
    """<p> The status of the current snapshot of the table. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""
    failure_description: NotRequired[
        "capo_firehose.types.failure_description.FailureDescription"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseSnapshotInfo) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Table"] = value["table"]
    import capo_firehose.types.timestamp

    out["RequestTimestamp"] = capo_firehose.types.timestamp.serialize_aws_json_1_1(
        value["request_timestamp"]
    )
    import capo_firehose.types.snapshot_requested_by

    out["RequestedBy"] = (
        capo_firehose.types.snapshot_requested_by.serialize_aws_json_1_1(
            value["requested_by"]
        )
    )
    import capo_firehose.types.snapshot_status

    out["Status"] = capo_firehose.types.snapshot_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "failure_description" in value:
        import capo_firehose.types.failure_description

        out["FailureDescription"] = (
            capo_firehose.types.failure_description.serialize_aws_json_1_1(
                value["failure_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseSnapshotInfo:
    out: DatabaseSnapshotInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DatabaseSnapshotInfo.id required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("DatabaseSnapshotInfo.table required")
    if "RequestTimestamp" in data:
        import capo_firehose.types.timestamp

        out["request_timestamp"] = (
            capo_firehose.types.timestamp.deserialize_aws_json_1_1(
                data["RequestTimestamp"]
            )
        )
    else:
        raise DeserializationError("DatabaseSnapshotInfo.request_timestamp required")
    if "RequestedBy" in data:
        import capo_firehose.types.snapshot_requested_by

        out["requested_by"] = (
            capo_firehose.types.snapshot_requested_by.deserialize_aws_json_1_1(
                data["RequestedBy"]
            )
        )
    else:
        raise DeserializationError("DatabaseSnapshotInfo.requested_by required")
    if "Status" in data:
        import capo_firehose.types.snapshot_status

        out["status"] = capo_firehose.types.snapshot_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        raise DeserializationError("DatabaseSnapshotInfo.status required")
    if "FailureDescription" in data:
        import capo_firehose.types.failure_description

        out["failure_description"] = (
            capo_firehose.types.failure_description.deserialize_aws_json_1_1(
                data["FailureDescription"]
            )
        )
    return out
