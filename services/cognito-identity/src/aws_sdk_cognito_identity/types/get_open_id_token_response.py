"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetOpenIdTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_id
    import aws_sdk_cognito_identity.types.oidc_token


class GetOpenIdTokenResponse(TypedDict, closed=True):
    identity_id: NotRequired["aws_sdk_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID. Note that the IdentityId returned may not match the one passed on input.</p>"""
    token: NotRequired["aws_sdk_cognito_identity.types.oidc_token.OIDCToken"]
    """<p>An OpenID token, valid for 10 minutes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpenIdTokenResponse) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "token" in value:
        out["Token"] = value["token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpenIdTokenResponse:
    out: GetOpenIdTokenResponse = {}  # type: ignore[typeddict-item]
    if "IdentityId" in data:
        out["identity_id"] = data["IdentityId"]
    if "Token" in data:
        out["token"] = data["Token"]
    return out
