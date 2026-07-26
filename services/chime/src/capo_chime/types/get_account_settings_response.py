"""Generated from Smithy shape ``com.amazonaws.chime#GetAccountSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.account_settings


class GetAccountSettingsResponse(TypedDict, closed=True):
    account_settings: NotRequired["capo_chime.types.account_settings.AccountSettings"]
    """<p>The Amazon Chime account settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountSettingsResponse) -> dict:
    out: dict = {}
    if "account_settings" in value:
        import capo_chime.types.account_settings

        out["AccountSettings"] = capo_chime.types.account_settings.serialize_json(
            value["account_settings"]
        )
    return out


def deserialize_json(data: dict) -> GetAccountSettingsResponse:
    out: GetAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if "AccountSettings" in data:
        import capo_chime.types.account_settings

        out["account_settings"] = capo_chime.types.account_settings.deserialize_json(
            data["AccountSettings"]
        )
    return out
