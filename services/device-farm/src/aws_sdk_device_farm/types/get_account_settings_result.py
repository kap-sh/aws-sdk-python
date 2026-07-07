"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetAccountSettingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.account_settings


class GetAccountSettingsResult(TypedDict, closed=True):
    account_settings: NotRequired[
        "aws_sdk_device_farm.types.account_settings.AccountSettings"
    ]
    """<p>The account settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountSettingsResult) -> dict:
    out: dict = {}
    if "account_settings" in value:
        import aws_sdk_device_farm.types.account_settings

        out["accountSettings"] = (
            aws_sdk_device_farm.types.account_settings.serialize_aws_json_1_1(
                value["account_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountSettingsResult:
    out: GetAccountSettingsResult = {}  # type: ignore[typeddict-item]
    if "accountSettings" in data:
        import aws_sdk_device_farm.types.account_settings

        out["account_settings"] = (
            aws_sdk_device_farm.types.account_settings.deserialize_aws_json_1_1(
                data["accountSettings"]
            )
        )
    return out
