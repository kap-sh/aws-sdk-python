"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileSystemRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.delete_file_system_lustre_configuration
    import aws_sdk_fsx.types.delete_file_system_open_zfs_configuration
    import aws_sdk_fsx.types.delete_file_system_windows_configuration
    import aws_sdk_fsx.types.file_system_id


class DeleteFileSystemRequest(TypedDict):
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    """<p>The ID of the file system that you want to delete.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    """<p>A string of up to 63 ASCII characters that Amazon FSx uses to ensure idempotent deletion. This token is automatically filled on your behalf when using the Command Line Interface (CLI) or an Amazon Web Services SDK.</p>"""
    windows_configuration: NotRequired[
        "aws_sdk_fsx.types.delete_file_system_windows_configuration.DeleteFileSystemWindowsConfiguration"
    ]
    lustre_configuration: NotRequired[
        "aws_sdk_fsx.types.delete_file_system_lustre_configuration.DeleteFileSystemLustreConfiguration"
    ]
    open_zfs_configuration: NotRequired[
        "aws_sdk_fsx.types.delete_file_system_open_zfs_configuration.DeleteFileSystemOpenZFSConfiguration"
    ]
    """<p>The configuration object for the OpenZFS file system used in the <code>DeleteFileSystem</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileSystemRequest) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "windows_configuration" in value:
        import aws_sdk_fsx.types.delete_file_system_windows_configuration

        out["WindowsConfiguration"] = (
            aws_sdk_fsx.types.delete_file_system_windows_configuration.serialize_aws_json_1_1(
                value["windows_configuration"]
            )
        )
    if "lustre_configuration" in value:
        import aws_sdk_fsx.types.delete_file_system_lustre_configuration

        out["LustreConfiguration"] = (
            aws_sdk_fsx.types.delete_file_system_lustre_configuration.serialize_aws_json_1_1(
                value["lustre_configuration"]
            )
        )
    if "open_zfs_configuration" in value:
        import aws_sdk_fsx.types.delete_file_system_open_zfs_configuration

        out["OpenZFSConfiguration"] = (
            aws_sdk_fsx.types.delete_file_system_open_zfs_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileSystemRequest:
    out: DeleteFileSystemRequest = {}  # type: ignore[typeddict-item]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "WindowsConfiguration" in data:
        import aws_sdk_fsx.types.delete_file_system_windows_configuration

        out["windows_configuration"] = (
            aws_sdk_fsx.types.delete_file_system_windows_configuration.deserialize_aws_json_1_1(
                data["WindowsConfiguration"]
            )
        )
    if "LustreConfiguration" in data:
        import aws_sdk_fsx.types.delete_file_system_lustre_configuration

        out["lustre_configuration"] = (
            aws_sdk_fsx.types.delete_file_system_lustre_configuration.deserialize_aws_json_1_1(
                data["LustreConfiguration"]
            )
        )
    if "OpenZFSConfiguration" in data:
        import aws_sdk_fsx.types.delete_file_system_open_zfs_configuration

        out["open_zfs_configuration"] = (
            aws_sdk_fsx.types.delete_file_system_open_zfs_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    return out
