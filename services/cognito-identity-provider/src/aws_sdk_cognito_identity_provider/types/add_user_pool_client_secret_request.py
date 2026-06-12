"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AddUserPoolClientSecretRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_id_type
    import aws_sdk_cognito_identity_provider.types.client_secret_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class AddUserPoolClientSecretRequest(TypedDict):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the app client.</p>"""
    client_id: "aws_sdk_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client for which you want to create a new secret.</p>"""
    client_secret: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_secret_type.ClientSecretType"
    ]
    """<p>The client secret value you want to use. If you don't provide this parameter, Amazon Cognito generates a secure secret for you.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddUserPoolClientSecretRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddUserPoolClientSecretRequest:
    out: AddUserPoolClientSecretRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "AddUserPoolClientSecretRequest.user_pool_id required"
        )
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("AddUserPoolClientSecretRequest.client_id required")
    if "ClientSecret" in data:
        out["client_secret"] = data["ClientSecret"]
    return out
