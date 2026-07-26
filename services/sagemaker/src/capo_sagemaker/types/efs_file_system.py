"""Generated from Smithy shape ``com.amazonaws.sagemaker#EFSFileSystem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.file_system_id


class EFSFileSystem(TypedDict, closed=True):
    file_system_id: NotRequired["capo_sagemaker.types.file_system_id.FileSystemId"]
    """<p>The ID of your Amazon EFS file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EFSFileSystem) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EFSFileSystem:
    out: EFSFileSystem = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    return out
