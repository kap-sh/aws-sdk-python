"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteWebAuthnCredentialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type
    import aws_sdk_cognito_identity_provider.types.token_model_type


class DeleteWebAuthnCredentialRequest(TypedDict, closed=True):
    access_token: (
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    )
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    credential_id: "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    """<p>The unique identifier of the passkey that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWebAuthnCredentialRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    out["CredentialId"] = value["credential_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWebAuthnCredentialRequest:
    out: DeleteWebAuthnCredentialRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError(
            "DeleteWebAuthnCredentialRequest.access_token required"
        )
    if "CredentialId" in data:
        out["credential_id"] = data["CredentialId"]
    else:
        raise DeserializationError(
            "DeleteWebAuthnCredentialRequest.credential_id required"
        )
    return out
