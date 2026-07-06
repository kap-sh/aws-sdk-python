"""Generated from Smithy shape ``com.amazonaws.sagemaker#FSxLustreFileSystem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.file_system_id


class FSxLustreFileSystem(TypedDict, closed=True):
    file_system_id: NotRequired["aws_sdk_sagemaker.types.file_system_id.FileSystemId"]
    """<p>Amazon FSx for Lustre file system ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FSxLustreFileSystem) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FSxLustreFileSystem:
    out: FSxLustreFileSystem = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    return out
