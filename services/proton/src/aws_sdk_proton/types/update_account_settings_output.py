"""Generated from Smithy shape ``com.amazonaws.proton#UpdateAccountSettingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.account_settings


class UpdateAccountSettingsOutput(TypedDict, closed=True):
    account_settings: "aws_sdk_proton.types.account_settings.AccountSettings"
    """<p>The Proton pipeline service role and repository data shared across the Amazon Web Services account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAccountSettingsOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.account_settings

    out["accountSettings"] = (
        aws_sdk_proton.types.account_settings.serialize_aws_json_1_0(
            value["account_settings"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAccountSettingsOutput:
    out: UpdateAccountSettingsOutput = {}  # type: ignore[typeddict-item]
    if "accountSettings" in data:
        import aws_sdk_proton.types.account_settings

        out["account_settings"] = (
            aws_sdk_proton.types.account_settings.deserialize_aws_json_1_0(
                data["accountSettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAccountSettingsOutput.account_settings required"
        )
    return out
