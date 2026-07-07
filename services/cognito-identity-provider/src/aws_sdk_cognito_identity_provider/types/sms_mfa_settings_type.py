"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SMSMfaSettingsType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.boolean_type


class SMSMfaSettingsType(TypedDict, closed=True):
    enabled: "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Specifies whether SMS message MFA is activated. If an MFA type is activated for a user, the user will be prompted for MFA during all sign-in attempts, unless device tracking is turned on and the device has been trusted.</p>"""
    preferred_mfa: "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Specifies whether SMS is the preferred MFA method. If true, your user pool prompts the specified user for a code delivered by SMS message after username-password sign-in succeeds. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SMSMfaSettingsType) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    out["PreferredMfa"] = value.get("preferred_mfa", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SMSMfaSettingsType:
    out: SMSMfaSettingsType = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if "PreferredMfa" in data:
        out["preferred_mfa"] = data["PreferredMfa"]
    else:
        out["preferred_mfa"] = False
    return out
