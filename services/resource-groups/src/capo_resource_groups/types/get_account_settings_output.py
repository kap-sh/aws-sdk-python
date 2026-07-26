"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetAccountSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.account_settings


class GetAccountSettingsOutput(TypedDict, closed=True):
    account_settings: NotRequired[
        "capo_resource_groups.types.account_settings.AccountSettings"
    ]
    """<p>The current settings for the optional features in Resource Groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountSettingsOutput) -> dict:
    out: dict = {}
    if "account_settings" in value:
        import capo_resource_groups.types.account_settings

        out["AccountSettings"] = (
            capo_resource_groups.types.account_settings.serialize_json(
                value["account_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAccountSettingsOutput:
    out: GetAccountSettingsOutput = {}  # type: ignore[typeddict-item]
    if "AccountSettings" in data:
        import capo_resource_groups.types.account_settings

        out["account_settings"] = (
            capo_resource_groups.types.account_settings.deserialize_json(
                data["AccountSettings"]
            )
        )
    return out
