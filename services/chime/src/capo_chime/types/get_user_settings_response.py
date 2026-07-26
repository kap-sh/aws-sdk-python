"""Generated from Smithy shape ``com.amazonaws.chime#GetUserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.user_settings


class GetUserSettingsResponse(TypedDict, closed=True):
    user_settings: NotRequired["capo_chime.types.user_settings.UserSettings"]
    """<p>The user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserSettingsResponse) -> dict:
    out: dict = {}
    if "user_settings" in value:
        import capo_chime.types.user_settings

        out["UserSettings"] = capo_chime.types.user_settings.serialize_json(
            value["user_settings"]
        )
    return out


def deserialize_json(data: dict) -> GetUserSettingsResponse:
    out: GetUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if "UserSettings" in data:
        import capo_chime.types.user_settings

        out["user_settings"] = capo_chime.types.user_settings.deserialize_json(
            data["UserSettings"]
        )
    return out
