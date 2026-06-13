"""Generated from Smithy shape ``com.amazonaws.proton#GetAccountSettingsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.account_settings


class GetAccountSettingsOutput(TypedDict):
    account_settings: NotRequired[
        "aws_sdk_proton.types.account_settings.AccountSettings"
    ]
    """<p>The Proton pipeline service role detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountSettingsOutput) -> dict:
    out: dict = {}
    if "account_settings" in value:
        import aws_sdk_proton.types.account_settings

        out["accountSettings"] = (
            aws_sdk_proton.types.account_settings.serialize_aws_json_1_0(
                value["account_settings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountSettingsOutput:
    out: GetAccountSettingsOutput = {}  # type: ignore[typeddict-item]
    if "accountSettings" in data:
        import aws_sdk_proton.types.account_settings

        out["account_settings"] = (
            aws_sdk_proton.types.account_settings.deserialize_aws_json_1_0(
                data["accountSettings"]
            )
        )
    return out
