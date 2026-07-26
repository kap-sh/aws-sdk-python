"""Generated from Smithy shape ``com.amazonaws.chime#UpdateAccountSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.account_settings
    import capo_chime.types.non_empty_string


class UpdateAccountSettingsRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    account_settings: "capo_chime.types.account_settings.AccountSettings"
    """<p>The Amazon Chime account settings to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountSettingsRequest) -> dict:
    out: dict = {}
    import capo_chime.types.account_settings

    out["AccountSettings"] = capo_chime.types.account_settings.serialize_json(
        value["account_settings"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAccountSettingsRequest:
    out: UpdateAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    if "AccountSettings" in data:
        import capo_chime.types.account_settings

        out["account_settings"] = capo_chime.types.account_settings.deserialize_json(
            data["AccountSettings"]
        )
    else:
        raise DeserializationError(
            "UpdateAccountSettingsRequest.account_settings required"
        )
    return out
