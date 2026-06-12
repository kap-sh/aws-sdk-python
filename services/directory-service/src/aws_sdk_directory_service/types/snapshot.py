"""Generated from Smithy shape ``com.amazonaws.directoryservice#Snapshot``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.snapshot_id
    import aws_sdk_directory_service.types.snapshot_name
    import aws_sdk_directory_service.types.snapshot_status
    import aws_sdk_directory_service.types.snapshot_type
    import aws_sdk_directory_service.types.start_time


class Snapshot(TypedDict):
    directory_id: NotRequired[
        "aws_sdk_directory_service.types.directory_id.DirectoryId"
    ]
    """<p>The directory identifier.</p>"""
    snapshot_id: NotRequired["aws_sdk_directory_service.types.snapshot_id.SnapshotId"]
    """<p>The snapshot identifier.</p>"""
    type: NotRequired["aws_sdk_directory_service.types.snapshot_type.SnapshotType"]
    """<p>The snapshot type.</p>"""
    name: NotRequired["aws_sdk_directory_service.types.snapshot_name.SnapshotName"]
    """<p>The descriptive name of the snapshot.</p>"""
    status: NotRequired[
        "aws_sdk_directory_service.types.snapshot_status.SnapshotStatus"
    ]
    """<p>The snapshot status.</p>"""
    start_time: NotRequired["aws_sdk_directory_service.types.start_time.StartTime"]
    """<p>The date and time that the snapshot was taken.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshot) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "type" in value:
        import aws_sdk_directory_service.types.snapshot_type

        out["Type"] = (
            aws_sdk_directory_service.types.snapshot_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_directory_service.types.snapshot_status

        out["Status"] = (
            aws_sdk_directory_service.types.snapshot_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import aws_sdk_directory_service.types.start_time

        out["StartTime"] = (
            aws_sdk_directory_service.types.start_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    if "Type" in data:
        import aws_sdk_directory_service.types.snapshot_type

        out["type"] = (
            aws_sdk_directory_service.types.snapshot_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_directory_service.types.snapshot_status

        out["status"] = (
            aws_sdk_directory_service.types.snapshot_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_directory_service.types.start_time

        out["start_time"] = (
            aws_sdk_directory_service.types.start_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    return out
