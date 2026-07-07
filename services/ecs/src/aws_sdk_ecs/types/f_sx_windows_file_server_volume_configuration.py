"""Generated from Smithy shape ``com.amazonaws.ecs#FSxWindowsFileServerVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.f_sx_windows_file_server_authorization_config
    import aws_sdk_ecs.types.string


class FSxWindowsFileServerVolumeConfiguration(TypedDict, closed=True):
    file_system_id: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon FSx for Windows File Server file system ID to use.</p>"""
    root_directory: "aws_sdk_ecs.types.string.String"
    """<p>The directory within the Amazon FSx for Windows File Server file system to mount as the root directory inside the host.</p>"""
    authorization_config: "aws_sdk_ecs.types.f_sx_windows_file_server_authorization_config.FSxWindowsFileServerAuthorizationConfig"
    """<p>The authorization configuration details for the Amazon FSx for Windows File Server file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FSxWindowsFileServerVolumeConfiguration) -> dict:
    out: dict = {}
    out["fileSystemId"] = value["file_system_id"]
    out["rootDirectory"] = value["root_directory"]
    import aws_sdk_ecs.types.f_sx_windows_file_server_authorization_config

    out["authorizationConfig"] = (
        aws_sdk_ecs.types.f_sx_windows_file_server_authorization_config.serialize_aws_json_1_1(
            value["authorization_config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FSxWindowsFileServerVolumeConfiguration:
    out: FSxWindowsFileServerVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if "fileSystemId" in data:
        out["file_system_id"] = data["fileSystemId"]
    else:
        raise DeserializationError(
            "FSxWindowsFileServerVolumeConfiguration.file_system_id required"
        )
    if "rootDirectory" in data:
        out["root_directory"] = data["rootDirectory"]
    else:
        raise DeserializationError(
            "FSxWindowsFileServerVolumeConfiguration.root_directory required"
        )
    if "authorizationConfig" in data:
        import aws_sdk_ecs.types.f_sx_windows_file_server_authorization_config

        out["authorization_config"] = (
            aws_sdk_ecs.types.f_sx_windows_file_server_authorization_config.deserialize_aws_json_1_1(
                data["authorizationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "FSxWindowsFileServerVolumeConfiguration.authorization_config required"
        )
    return out
