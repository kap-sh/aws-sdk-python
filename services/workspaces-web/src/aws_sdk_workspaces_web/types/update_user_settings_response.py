"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateUserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.user_settings


class UpdateUserSettingsResponse(TypedDict, closed=True):
    user_settings: "aws_sdk_workspaces_web.types.user_settings.UserSettings"
    """<p>The user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserSettingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_web.types.user_settings

    out["userSettings"] = aws_sdk_workspaces_web.types.user_settings.serialize_json(
        value["user_settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateUserSettingsResponse:
    out: UpdateUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "userSettings" in data:
        import aws_sdk_workspaces_web.types.user_settings

        out["user_settings"] = (
            aws_sdk_workspaces_web.types.user_settings.deserialize_json(
                data["userSettings"]
            )
        )
    else:
        raise DeserializationError("UpdateUserSettingsResponse.user_settings required")
    return out
