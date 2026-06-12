"""Generated from Smithy shape ``com.amazonaws.chime#GetUserSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.user_settings


class GetUserSettingsResponse(TypedDict):
    user_settings: NotRequired["aws_sdk_chime.types.user_settings.UserSettings"]
    """<p>The user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserSettingsResponse) -> dict:
    out: dict = {}
    if "user_settings" in value:
        import aws_sdk_chime.types.user_settings

        out["UserSettings"] = aws_sdk_chime.types.user_settings.serialize_json(
            value["user_settings"]
        )
    return out


def deserialize_json(data: dict) -> GetUserSettingsResponse:
    out: GetUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "UserSettings" in data:
        import aws_sdk_chime.types.user_settings

        out["user_settings"] = aws_sdk_chime.types.user_settings.deserialize_json(
            data["UserSettings"]
        )
    return out
