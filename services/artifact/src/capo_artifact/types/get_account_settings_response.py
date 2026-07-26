"""Generated from Smithy shape ``com.amazonaws.artifact#GetAccountSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_artifact.types.account_settings


class GetAccountSettingsResponse(TypedDict, closed=True):
    account_settings: NotRequired[
        "capo_artifact.types.account_settings.AccountSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountSettingsResponse) -> dict:
    out: dict = {}
    if "account_settings" in value:
        import capo_artifact.types.account_settings

        out["accountSettings"] = capo_artifact.types.account_settings.serialize_json(
            value["account_settings"]
        )
    return out


def deserialize_json(data: dict) -> GetAccountSettingsResponse:
    out: GetAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if "accountSettings" in data:
        import capo_artifact.types.account_settings

        out["account_settings"] = capo_artifact.types.account_settings.deserialize_json(
            data["accountSettings"]
        )
    return out
