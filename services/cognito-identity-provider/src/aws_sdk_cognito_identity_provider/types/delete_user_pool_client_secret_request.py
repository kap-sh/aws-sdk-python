"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteUserPoolClientSecretRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_id_type
    import aws_sdk_cognito_identity_provider.types.client_secret_id_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class DeleteUserPoolClientSecretRequest(TypedDict):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the app client.</p>"""
    client_id: "aws_sdk_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client from which you want to delete the secret.</p>"""
    client_secret_id: "aws_sdk_cognito_identity_provider.types.client_secret_id_type.ClientSecretIdType"
    """<p>The unique identifier of the client secret you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserPoolClientSecretRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    out["ClientSecretId"] = value["client_secret_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserPoolClientSecretRequest:
    out: DeleteUserPoolClientSecretRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DeleteUserPoolClientSecretRequest.user_pool_id required"
        )
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError(
            "DeleteUserPoolClientSecretRequest.client_id required"
        )
    if "ClientSecretId" in data:
        out["client_secret_id"] = data["ClientSecretId"]
    else:
        raise DeserializationError(
            "DeleteUserPoolClientSecretRequest.client_secret_id required"
        )
    return out
