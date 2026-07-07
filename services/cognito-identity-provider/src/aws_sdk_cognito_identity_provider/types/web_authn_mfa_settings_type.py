"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnMfaSettingsType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.boolean_type


class WebAuthnMfaSettingsType(TypedDict, closed=True):
    enabled: "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Specifies whether passkey MFA is activated for a user. When activated, the user's passkey authentication requires user verification, and passkey sign-in is available when MFA is required. The user must also have at least one other MFA method such as SMS, TOTP, or email activated to prevent account lockout.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnMfaSettingsType) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> WebAuthnMfaSettingsType:
    out: WebAuthnMfaSettingsType = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
