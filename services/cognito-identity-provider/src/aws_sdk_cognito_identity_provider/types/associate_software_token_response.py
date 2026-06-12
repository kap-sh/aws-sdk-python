"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssociateSoftwareTokenResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.secret_code_type
    import aws_sdk_cognito_identity_provider.types.session_type


class AssociateSoftwareTokenResponse(TypedDict):
    secret_code: NotRequired[
        "aws_sdk_cognito_identity_provider.types.secret_code_type.SecretCodeType"
    ]
    """<p>A unique generated shared secret code that is used by the TOTP algorithm to generate a one-time code.</p>"""
    session: NotRequired[
        "aws_sdk_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>The session identifier that maintains the state of authentication requests and challenge responses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateSoftwareTokenResponse) -> dict:
    out: dict = {}
    if "secret_code" in value:
        out["SecretCode"] = value["secret_code"]
    if "session" in value:
        out["Session"] = value["session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateSoftwareTokenResponse:
    out: AssociateSoftwareTokenResponse = {}  # type: ignore[typeddict-item]
    if "SecretCode" in data:
        out["secret_code"] = data["SecretCode"]
    if "Session" in data:
        out["session"] = data["Session"]
    return out
