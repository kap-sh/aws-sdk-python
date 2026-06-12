"""Generated from Smithy shape ``com.amazonaws.workspaces#ApplicationSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.application_settings_status_enum
    import aws_sdk_workspaces.types.settings_group


class ApplicationSettingsRequest(TypedDict):
    status: "aws_sdk_workspaces.types.application_settings_status_enum.ApplicationSettingsStatusEnum"
    """<p>Enables or disables persistent application settings for users during their pool sessions.</p>"""
    settings_group: NotRequired["aws_sdk_workspaces.types.settings_group.SettingsGroup"]
    """<p>The path prefix for the S3 bucket where users’ persistent application settings are stored. You can allow the same persistent application settings to be used across multiple pools by specifying the same settings group for each pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSettingsRequest) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.application_settings_status_enum

    out["Status"] = (
        aws_sdk_workspaces.types.application_settings_status_enum.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "settings_group" in value:
        out["SettingsGroup"] = value["settings_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSettingsRequest:
    out: ApplicationSettingsRequest = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_workspaces.types.application_settings_status_enum

        out["status"] = (
            aws_sdk_workspaces.types.application_settings_status_enum.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ApplicationSettingsRequest.status required")
    if "SettingsGroup" in data:
        out["settings_group"] = data["SettingsGroup"]
    return out
