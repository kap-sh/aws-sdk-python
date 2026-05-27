"""Generated from Smithy shape ``com.amazonaws.ecs#FSxWindowsFileServerVolumeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.f_sx_windows_file_server_authorization_config
    import aws_sdk_ecs.types.string


class FSxWindowsFileServerVolumeConfiguration(TypedDict):
    file_system_id: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon FSx for Windows File Server file system ID to use.</p>"""
    root_directory: "aws_sdk_ecs.types.string.String"
    """<p>The directory within the Amazon FSx for Windows File Server file system to mount as the root directory inside the host.</p>"""
    authorization_config: "aws_sdk_ecs.types.f_sx_windows_file_server_authorization_config.FSxWindowsFileServerAuthorizationConfig"
    """<p>The authorization configuration details for the Amazon FSx for Windows File Server file system.</p>"""
