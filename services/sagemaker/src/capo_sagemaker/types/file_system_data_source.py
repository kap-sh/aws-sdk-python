"""Generated from Smithy shape ``com.amazonaws.sagemaker#FileSystemDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.directory_path
    import capo_sagemaker.types.file_system_access_mode
    import capo_sagemaker.types.file_system_id
    import capo_sagemaker.types.file_system_type


class FileSystemDataSource(TypedDict, closed=True):
    file_system_id: NotRequired["capo_sagemaker.types.file_system_id.FileSystemId"]
    """<p>The file system id.</p>"""
    file_system_access_mode: NotRequired[
        "capo_sagemaker.types.file_system_access_mode.FileSystemAccessMode"
    ]
    """<p>The access mode of the mount of the directory associated with the channel. A directory can be mounted either in <code>ro</code> (read-only) or <code>rw</code> (read-write) mode.</p>"""
    file_system_type: NotRequired[
        "capo_sagemaker.types.file_system_type.FileSystemType"
    ]
    """<p>The file system type. </p>"""
    directory_path: NotRequired["capo_sagemaker.types.directory_path.DirectoryPath"]
    """<p>The full path to the directory to associate with the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemDataSource) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "file_system_access_mode" in value:
        import capo_sagemaker.types.file_system_access_mode

        out["FileSystemAccessMode"] = (
            capo_sagemaker.types.file_system_access_mode.serialize_aws_json_1_1(
                value["file_system_access_mode"]
            )
        )
    if "file_system_type" in value:
        import capo_sagemaker.types.file_system_type

        out["FileSystemType"] = (
            capo_sagemaker.types.file_system_type.serialize_aws_json_1_1(
                value["file_system_type"]
            )
        )
    if "directory_path" in value:
        out["DirectoryPath"] = value["directory_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemDataSource:
    out: FileSystemDataSource = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "FileSystemAccessMode" in data:
        import capo_sagemaker.types.file_system_access_mode

        out["file_system_access_mode"] = (
            capo_sagemaker.types.file_system_access_mode.deserialize_aws_json_1_1(
                data["FileSystemAccessMode"]
            )
        )
    if "FileSystemType" in data:
        import capo_sagemaker.types.file_system_type

        out["file_system_type"] = (
            capo_sagemaker.types.file_system_type.deserialize_aws_json_1_1(
                data["FileSystemType"]
            )
        )
    if "DirectoryPath" in data:
        out["directory_path"] = data["DirectoryPath"]
    return out
