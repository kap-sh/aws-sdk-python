"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteUserPoolClientRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_id_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class DeleteUserPoolClientRequest(TypedDict):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to delete the client.</p>"""
    client_id: "aws_sdk_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the user pool app client that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserPoolClientRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserPoolClientRequest:
    out: DeleteUserPoolClientRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("DeleteUserPoolClientRequest.user_pool_id required")
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("DeleteUserPoolClientRequest.client_id required")
    return out
