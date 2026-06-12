"""Generated from Smithy shape ``com.amazonaws.sagemaker#FSxLustreFileSystemConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.file_system_id
    import aws_sdk_sagemaker.types.file_system_path


class FSxLustreFileSystemConfig(TypedDict):
    file_system_id: NotRequired["aws_sdk_sagemaker.types.file_system_id.FileSystemId"]
    """<p>The globally unique, 17-digit, ID of the file system, assigned by Amazon FSx for Lustre.</p>"""
    file_system_path: NotRequired[
        "aws_sdk_sagemaker.types.file_system_path.FileSystemPath"
    ]
    """<p>The path to the file system directory that is accessible in Amazon SageMaker Studio. Permitted users can access only this directory and below.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FSxLustreFileSystemConfig) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "file_system_path" in value:
        out["FileSystemPath"] = value["file_system_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FSxLustreFileSystemConfig:
    out: FSxLustreFileSystemConfig = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "FileSystemPath" in data:
        out["file_system_path"] = data["FileSystemPath"]
    return out
