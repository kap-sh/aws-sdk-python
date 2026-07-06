"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AccountRecoverySettingType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.recovery_mechanisms_type


class AccountRecoverySettingType(TypedDict, closed=True):
    recovery_mechanisms: NotRequired[
        "aws_sdk_cognito_identity_provider.types.recovery_mechanisms_type.RecoveryMechanismsType"
    ]
    """<p>The list of options and priorities for user message delivery in forgot-password operations. Sets or displays user pool preferences for email or SMS message priority, whether users should fall back to a second delivery method, and whether passwords should only be reset by administrators.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountRecoverySettingType) -> dict:
    out: dict = {}
    if "recovery_mechanisms" in value:
        import aws_sdk_cognito_identity_provider.types.recovery_mechanisms_type

        out["RecoveryMechanisms"] = (
            aws_sdk_cognito_identity_provider.types.recovery_mechanisms_type.serialize_aws_json_1_1(
                value["recovery_mechanisms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountRecoverySettingType:
    out: AccountRecoverySettingType = {}  # type: ignore[typeddict-item]
    if "RecoveryMechanisms" in data:
        import aws_sdk_cognito_identity_provider.types.recovery_mechanisms_type

        out["recovery_mechanisms"] = (
            aws_sdk_cognito_identity_provider.types.recovery_mechanisms_type.deserialize_aws_json_1_1(
                data["RecoveryMechanisms"]
            )
        )
    return out
