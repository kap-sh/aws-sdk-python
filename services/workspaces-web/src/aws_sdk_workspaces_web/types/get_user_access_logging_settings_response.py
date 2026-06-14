"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetUserAccessLoggingSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.user_access_logging_settings


class GetUserAccessLoggingSettingsResponse(TypedDict):
    user_access_logging_settings: NotRequired[
        "aws_sdk_workspaces_web.types.user_access_logging_settings.UserAccessLoggingSettings"
    ]
    """<p>The user access logging settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserAccessLoggingSettingsResponse) -> dict:
    out: dict = {}
    if "user_access_logging_settings" in value:
        import aws_sdk_workspaces_web.types.user_access_logging_settings

        out["userAccessLoggingSettings"] = (
            aws_sdk_workspaces_web.types.user_access_logging_settings.serialize_json(
                value["user_access_logging_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetUserAccessLoggingSettingsResponse:
    out: GetUserAccessLoggingSettingsResponse = {}  # type: ignore[typeddict-item]
    if "userAccessLoggingSettings" in data:
        import aws_sdk_workspaces_web.types.user_access_logging_settings

        out["user_access_logging_settings"] = (
            aws_sdk_workspaces_web.types.user_access_logging_settings.deserialize_json(
                data["userAccessLoggingSettings"]
            )
        )
    return out
