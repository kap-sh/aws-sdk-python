"""Generated from Smithy shape ``com.amazonaws.chime#UpdateUserSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.string
    import capo_chime.types.user_settings


class UpdateUserSettingsRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.string.String"
    """<p>The Amazon Chime account ID.</p>"""
    user_id: "capo_chime.types.string.String"
    """<p>The user ID.</p>"""
    user_settings: "capo_chime.types.user_settings.UserSettings"
    """<p>The user settings to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserSettingsRequest) -> dict:
    out: dict = {}
    import capo_chime.types.user_settings

    out["UserSettings"] = capo_chime.types.user_settings.serialize_json(
        value["user_settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateUserSettingsRequest:
    out: UpdateUserSettingsRequest = {}  # type: ignore[typeddict-item]
    if "UserSettings" in data:
        import capo_chime.types.user_settings

        out["user_settings"] = capo_chime.types.user_settings.deserialize_json(
            data["UserSettings"]
        )
    else:
        raise DeserializationError("UpdateUserSettingsRequest.user_settings required")
    return out
