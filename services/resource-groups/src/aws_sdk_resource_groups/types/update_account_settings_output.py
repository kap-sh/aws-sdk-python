"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UpdateAccountSettingsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.account_settings


class UpdateAccountSettingsOutput(TypedDict):
    account_settings: NotRequired[
        "aws_sdk_resource_groups.types.account_settings.AccountSettings"
    ]
    """<p>A structure that displays the status of the optional features in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountSettingsOutput) -> dict:
    out: dict = {}
    if "account_settings" in value:
        import aws_sdk_resource_groups.types.account_settings

        out["AccountSettings"] = (
            aws_sdk_resource_groups.types.account_settings.serialize_json(
                value["account_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountSettingsOutput:
    out: UpdateAccountSettingsOutput = {}  # type: ignore[typeddict-item]
    if "AccountSettings" in data:
        import aws_sdk_resource_groups.types.account_settings

        out["account_settings"] = (
            aws_sdk_resource_groups.types.account_settings.deserialize_json(
                data["AccountSettings"]
            )
        )
    return out
