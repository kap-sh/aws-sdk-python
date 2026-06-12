"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateDirectorySetupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.create_snapshot_before_update
    import aws_sdk_directory_service.types.directory_id
    import aws_sdk_directory_service.types.directory_size_update_settings
    import aws_sdk_directory_service.types.network_update_settings
    import aws_sdk_directory_service.types.os_update_settings
    import aws_sdk_directory_service.types.update_type


class UpdateDirectorySetupRequest(TypedDict):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory to update.</p>"""
    update_type: "aws_sdk_directory_service.types.update_type.UpdateType"
    """<p>The type of update to perform on the directory.</p>"""
    os_update_settings: NotRequired[
        "aws_sdk_directory_service.types.os_update_settings.OSUpdateSettings"
    ]
    """<p>Operating system configuration to apply during the directory update operation.</p>"""
    directory_size_update_settings: NotRequired[
        "aws_sdk_directory_service.types.directory_size_update_settings.DirectorySizeUpdateSettings"
    ]
    """<p>Directory size configuration to apply during the update operation.</p>"""
    network_update_settings: NotRequired[
        "aws_sdk_directory_service.types.network_update_settings.NetworkUpdateSettings"
    ]
    """<p>Network configuration to apply during the directory update operation.</p>"""
    create_snapshot_before_update: NotRequired[
        "aws_sdk_directory_service.types.create_snapshot_before_update.CreateSnapshotBeforeUpdate"
    ]
    """<p>Specifies whether to create a directory snapshot before performing the update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDirectorySetupRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    import aws_sdk_directory_service.types.update_type

    out["UpdateType"] = (
        aws_sdk_directory_service.types.update_type.serialize_aws_json_1_1(
            value["update_type"]
        )
    )
    if "os_update_settings" in value:
        import aws_sdk_directory_service.types.os_update_settings

        out["OSUpdateSettings"] = (
            aws_sdk_directory_service.types.os_update_settings.serialize_aws_json_1_1(
                value["os_update_settings"]
            )
        )
    if "directory_size_update_settings" in value:
        import aws_sdk_directory_service.types.directory_size_update_settings

        out["DirectorySizeUpdateSettings"] = (
            aws_sdk_directory_service.types.directory_size_update_settings.serialize_aws_json_1_1(
                value["directory_size_update_settings"]
            )
        )
    if "network_update_settings" in value:
        import aws_sdk_directory_service.types.network_update_settings

        out["NetworkUpdateSettings"] = (
            aws_sdk_directory_service.types.network_update_settings.serialize_aws_json_1_1(
                value["network_update_settings"]
            )
        )
    if "create_snapshot_before_update" in value:
        out["CreateSnapshotBeforeUpdate"] = value["create_snapshot_before_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDirectorySetupRequest:
    out: UpdateDirectorySetupRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("UpdateDirectorySetupRequest.directory_id required")
    if "UpdateType" in data:
        import aws_sdk_directory_service.types.update_type

        out["update_type"] = (
            aws_sdk_directory_service.types.update_type.deserialize_aws_json_1_1(
                data["UpdateType"]
            )
        )
    else:
        raise DeserializationError("UpdateDirectorySetupRequest.update_type required")
    if "OSUpdateSettings" in data:
        import aws_sdk_directory_service.types.os_update_settings

        out["os_update_settings"] = (
            aws_sdk_directory_service.types.os_update_settings.deserialize_aws_json_1_1(
                data["OSUpdateSettings"]
            )
        )
    if "DirectorySizeUpdateSettings" in data:
        import aws_sdk_directory_service.types.directory_size_update_settings

        out["directory_size_update_settings"] = (
            aws_sdk_directory_service.types.directory_size_update_settings.deserialize_aws_json_1_1(
                data["DirectorySizeUpdateSettings"]
            )
        )
    if "NetworkUpdateSettings" in data:
        import aws_sdk_directory_service.types.network_update_settings

        out["network_update_settings"] = (
            aws_sdk_directory_service.types.network_update_settings.deserialize_aws_json_1_1(
                data["NetworkUpdateSettings"]
            )
        )
    if "CreateSnapshotBeforeUpdate" in data:
        out["create_snapshot_before_update"] = data["CreateSnapshotBeforeUpdate"]
    return out
