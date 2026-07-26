"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SoftwareTokenMfaConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type


class SoftwareTokenMfaConfigType(TypedDict, closed=True):
    enabled: "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>The activation state of TOTP MFA.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SoftwareTokenMfaConfigType) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SoftwareTokenMfaConfigType:
    out: SoftwareTokenMfaConfigType = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
