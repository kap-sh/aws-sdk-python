"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RevokeTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_id_type
    import aws_sdk_cognito_identity_provider.types.client_secret_type
    import aws_sdk_cognito_identity_provider.types.token_model_type


class RevokeTokenRequest(TypedDict, closed=True):
    token: "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>The refresh token that you want to revoke.</p>"""
    client_id: "aws_sdk_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client where the token that you want to revoke was issued.</p>"""
    client_secret: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_secret_type.ClientSecretType"
    ]
    """<p>The client secret of the requested app client, if the client has a secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeTokenRequest) -> dict:
    out: dict = {}
    out["Token"] = value["token"]
    out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeTokenRequest:
    out: RevokeTokenRequest = {}  # type: ignore[typeddict-item]
    if "Token" in data:
        out["token"] = data["Token"]
    else:
        raise DeserializationError("RevokeTokenRequest.token required")
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("RevokeTokenRequest.client_id required")
    if "ClientSecret" in data:
        out["client_secret"] = data["ClientSecret"]
    return out
