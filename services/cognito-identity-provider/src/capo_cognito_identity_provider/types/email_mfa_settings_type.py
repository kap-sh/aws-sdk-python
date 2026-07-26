"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EmailMfaSettingsType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type


class EmailMfaSettingsType(TypedDict, closed=True):
    enabled: "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Specifies whether email message MFA is active for a user. When the value of this parameter is <code>Enabled</code>, the user will be prompted for MFA during all sign-in attempts, unless device tracking is turned on and the device has been trusted.</p>"""
    preferred_mfa: "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Specifies whether email message MFA is the user's preferred method.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmailMfaSettingsType) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    out["PreferredMfa"] = value.get("preferred_mfa", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> EmailMfaSettingsType:
    out: EmailMfaSettingsType = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if "PreferredMfa" in data:
        out["preferred_mfa"] = data["PreferredMfa"]
    else:
        out["preferred_mfa"] = False
    return out
