"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateUserAccessLoggingSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.user_access_logging_settings


class UpdateUserAccessLoggingSettingsResponse(TypedDict, closed=True):
    user_access_logging_settings: "capo_workspaces_web.types.user_access_logging_settings.UserAccessLoggingSettings"
    """<p>The user access logging settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserAccessLoggingSettingsResponse) -> dict:
    out: dict = {}
    import capo_workspaces_web.types.user_access_logging_settings

    out["userAccessLoggingSettings"] = (
        capo_workspaces_web.types.user_access_logging_settings.serialize_json(
            value["user_access_logging_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateUserAccessLoggingSettingsResponse:
    out: UpdateUserAccessLoggingSettingsResponse = {}  # type: ignore[typeddict-item]
    if "userAccessLoggingSettings" in data:
        import capo_workspaces_web.types.user_access_logging_settings

        out["user_access_logging_settings"] = (
            capo_workspaces_web.types.user_access_logging_settings.deserialize_json(
                data["userAccessLoggingSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateUserAccessLoggingSettingsResponse.user_access_logging_settings required"
        )
    return out
