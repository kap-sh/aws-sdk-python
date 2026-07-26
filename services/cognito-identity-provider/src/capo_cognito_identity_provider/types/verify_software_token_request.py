"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerifySoftwareTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.session_type
    import capo_cognito_identity_provider.types.software_token_mfa_user_code_type
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.token_model_type


class VerifySoftwareTokenRequest(TypedDict, closed=True):
    access_token: NotRequired[
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    session: NotRequired[
        "capo_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>The session ID from an <code>AssociateSoftwareToken</code> request.</p>"""
    user_code: "capo_cognito_identity_provider.types.software_token_mfa_user_code_type.SoftwareTokenMFAUserCodeType"
    """<p>A TOTP that the user generated in their configured authenticator app.</p>"""
    friendly_device_name: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>A friendly name for the device that's running the TOTP authenticator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifySoftwareTokenRequest) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    if "session" in value:
        out["Session"] = value["session"]
    out["UserCode"] = value["user_code"]
    if "friendly_device_name" in value:
        out["FriendlyDeviceName"] = value["friendly_device_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifySoftwareTokenRequest:
    out: VerifySoftwareTokenRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    if "Session" in data:
        out["session"] = data["Session"]
    if "UserCode" in data:
        out["user_code"] = data["UserCode"]
    else:
        raise DeserializationError("VerifySoftwareTokenRequest.user_code required")
    if "FriendlyDeviceName" in data:
        out["friendly_device_name"] = data["FriendlyDeviceName"]
    return out
