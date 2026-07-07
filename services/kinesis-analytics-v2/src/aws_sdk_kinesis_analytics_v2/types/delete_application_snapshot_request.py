"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.snapshot_name
    import aws_sdk_kinesis_analytics_v2.types.timestamp


class DeleteApplicationSnapshotRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of an existing application.</p>"""
    snapshot_name: "aws_sdk_kinesis_analytics_v2.types.snapshot_name.SnapshotName"
    """<p>The identifier for the snapshot delete.</p>"""
    snapshot_creation_timestamp: (
        "aws_sdk_kinesis_analytics_v2.types.timestamp.Timestamp"
    )
    """<p>The creation timestamp of the application snapshot to delete. You can retrieve this value using or .</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationSnapshotRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["SnapshotName"] = value["snapshot_name"]
    import aws_sdk_kinesis_analytics_v2.types.timestamp

    out["SnapshotCreationTimestamp"] = (
        aws_sdk_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["snapshot_creation_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationSnapshotRequest:
    out: DeleteApplicationSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DeleteApplicationSnapshotRequest.application_name required"
        )
    if "SnapshotName" in data:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        raise DeserializationError(
            "DeleteApplicationSnapshotRequest.snapshot_name required"
        )
    if "SnapshotCreationTimestamp" in data:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["snapshot_creation_timestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["SnapshotCreationTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteApplicationSnapshotRequest.snapshot_creation_timestamp required"
        )
    return out
