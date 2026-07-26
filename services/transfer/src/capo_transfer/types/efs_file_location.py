"""Generated from Smithy shape ``com.amazonaws.transfer#EfsFileLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.efs_file_system_id
    import capo_transfer.types.efs_path


class EfsFileLocation(TypedDict, closed=True):
    file_system_id: NotRequired[
        "capo_transfer.types.efs_file_system_id.EfsFileSystemId"
    ]
    """<p>The identifier of the file system, assigned by Amazon EFS.</p>"""
    path: NotRequired["capo_transfer.types.efs_path.EfsPath"]
    """<p>The pathname for the folder being used by a workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EfsFileLocation) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EfsFileLocation:
    out: EfsFileLocation = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Path" in data:
        out["path"] = data["Path"]
    return out
