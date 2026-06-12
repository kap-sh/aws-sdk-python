"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileSystemResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.delete_file_system_lustre_response
    import aws_sdk_fsx.types.delete_file_system_open_zfs_response
    import aws_sdk_fsx.types.delete_file_system_windows_response
    import aws_sdk_fsx.types.file_system_id
    import aws_sdk_fsx.types.file_system_lifecycle


class DeleteFileSystemResponse(TypedDict):
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    """<p>The ID of the file system that's being deleted.</p>"""
    lifecycle: NotRequired[
        "aws_sdk_fsx.types.file_system_lifecycle.FileSystemLifecycle"
    ]
    """<p>The file system lifecycle for the deletion request. If the <code>DeleteFileSystem</code> operation is successful, this status is <code>DELETING</code>.</p>"""
    windows_response: NotRequired[
        "aws_sdk_fsx.types.delete_file_system_windows_response.DeleteFileSystemWindowsResponse"
    ]
    lustre_response: NotRequired[
        "aws_sdk_fsx.types.delete_file_system_lustre_response.DeleteFileSystemLustreResponse"
    ]
    open_zfs_response: NotRequired[
        "aws_sdk_fsx.types.delete_file_system_open_zfs_response.DeleteFileSystemOpenZFSResponse"
    ]
    """<p>The response object for the OpenZFS file system that's being deleted in the <code>DeleteFileSystem</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileSystemResponse) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.file_system_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.file_system_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "windows_response" in value:
        import aws_sdk_fsx.types.delete_file_system_windows_response

        out["WindowsResponse"] = (
            aws_sdk_fsx.types.delete_file_system_windows_response.serialize_aws_json_1_1(
                value["windows_response"]
            )
        )
    if "lustre_response" in value:
        import aws_sdk_fsx.types.delete_file_system_lustre_response

        out["LustreResponse"] = (
            aws_sdk_fsx.types.delete_file_system_lustre_response.serialize_aws_json_1_1(
                value["lustre_response"]
            )
        )
    if "open_zfs_response" in value:
        import aws_sdk_fsx.types.delete_file_system_open_zfs_response

        out["OpenZFSResponse"] = (
            aws_sdk_fsx.types.delete_file_system_open_zfs_response.serialize_aws_json_1_1(
                value["open_zfs_response"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileSystemResponse:
    out: DeleteFileSystemResponse = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.file_system_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.file_system_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "WindowsResponse" in data:
        import aws_sdk_fsx.types.delete_file_system_windows_response

        out["windows_response"] = (
            aws_sdk_fsx.types.delete_file_system_windows_response.deserialize_aws_json_1_1(
                data["WindowsResponse"]
            )
        )
    if "LustreResponse" in data:
        import aws_sdk_fsx.types.delete_file_system_lustre_response

        out["lustre_response"] = (
            aws_sdk_fsx.types.delete_file_system_lustre_response.deserialize_aws_json_1_1(
                data["LustreResponse"]
            )
        )
    if "OpenZFSResponse" in data:
        import aws_sdk_fsx.types.delete_file_system_open_zfs_response

        out["open_zfs_response"] = (
            aws_sdk_fsx.types.delete_file_system_open_zfs_response.deserialize_aws_json_1_1(
                data["OpenZFSResponse"]
            )
        )
    return out
