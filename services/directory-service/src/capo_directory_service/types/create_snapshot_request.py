"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.snapshot_name


class CreateSnapshotRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory of which to take a snapshot.</p>"""
    name: NotRequired["capo_directory_service.types.snapshot_name.SnapshotName"]
    """<p>The descriptive name to apply to the snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotRequest:
    out: CreateSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("CreateSnapshotRequest.directory_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    return out
