"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssociateSoftwareTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.session_type
    import capo_cognito_identity_provider.types.token_model_type


class AssociateSoftwareTokenRequest(TypedDict, closed=True):
    access_token: NotRequired[
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p> <p>You can provide either an access token or a session ID in the request.</p>"""
    session: NotRequired[
        "capo_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>The session identifier that maintains the state of authentication requests and challenge responses. In <code>AssociateSoftwareToken</code>, this is the session ID from a successful sign-in. You can provide either an access token or a session ID in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateSoftwareTokenRequest) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    if "session" in value:
        out["Session"] = value["session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateSoftwareTokenRequest:
    out: AssociateSoftwareTokenRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    if "Session" in data:
        out["session"] = data["Session"]
    return out
