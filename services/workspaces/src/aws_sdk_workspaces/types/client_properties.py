"""Generated from Smithy shape ``com.amazonaws.workspaces#ClientProperties``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.log_upload_enum
    import aws_sdk_workspaces.types.reconnect_enum


class ClientProperties(TypedDict):
    reconnect_enabled: NotRequired[
        "aws_sdk_workspaces.types.reconnect_enum.ReconnectEnum"
    ]
    """<p>Specifies whether users can cache their credentials on the Amazon WorkSpaces client. When enabled, users can choose to reconnect to their WorkSpaces without re-entering their credentials. </p>"""
    log_upload_enabled: NotRequired[
        "aws_sdk_workspaces.types.log_upload_enum.LogUploadEnum"
    ]
    """<p>Specifies whether users can upload diagnostic log files of Amazon WorkSpaces client directly to WorkSpaces to troubleshoot issues when using the WorkSpaces client. When enabled, the log files will be sent to WorkSpaces automatically and will be applied to all users in the specified directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientProperties) -> dict:
    out: dict = {}
    if "reconnect_enabled" in value:
        import aws_sdk_workspaces.types.reconnect_enum

        out["ReconnectEnabled"] = (
            aws_sdk_workspaces.types.reconnect_enum.serialize_aws_json_1_1(
                value["reconnect_enabled"]
            )
        )
    if "log_upload_enabled" in value:
        import aws_sdk_workspaces.types.log_upload_enum

        out["LogUploadEnabled"] = (
            aws_sdk_workspaces.types.log_upload_enum.serialize_aws_json_1_1(
                value["log_upload_enabled"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientProperties:
    out: ClientProperties = {}  # type: ignore[typeddict-item]
    if "ReconnectEnabled" in data:
        import aws_sdk_workspaces.types.reconnect_enum

        out["reconnect_enabled"] = (
            aws_sdk_workspaces.types.reconnect_enum.deserialize_aws_json_1_1(
                data["ReconnectEnabled"]
            )
        )
    if "LogUploadEnabled" in data:
        import aws_sdk_workspaces.types.log_upload_enum

        out["log_upload_enabled"] = (
            aws_sdk_workspaces.types.log_upload_enum.deserialize_aws_json_1_1(
                data["LogUploadEnabled"]
            )
        )
    return out
