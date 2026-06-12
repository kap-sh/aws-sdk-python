"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminDisableProviderForUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.provider_user_identifier_type
    import aws_sdk_cognito_identity_provider.types.string_type


class AdminDisableProviderForUserRequest(TypedDict):
    user_pool_id: "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    """<p>The ID of the user pool where you want to delete the user's linked identities.</p>"""
    user: "aws_sdk_cognito_identity_provider.types.provider_user_identifier_type.ProviderUserIdentifierType"
    """<p>The user profile that you want to delete a linked identity from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminDisableProviderForUserRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    import aws_sdk_cognito_identity_provider.types.provider_user_identifier_type

    out["User"] = (
        aws_sdk_cognito_identity_provider.types.provider_user_identifier_type.serialize_aws_json_1_1(
            value["user"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminDisableProviderForUserRequest:
    out: AdminDisableProviderForUserRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "AdminDisableProviderForUserRequest.user_pool_id required"
        )
    if "User" in data:
        import aws_sdk_cognito_identity_provider.types.provider_user_identifier_type

        out["user"] = (
            aws_sdk_cognito_identity_provider.types.provider_user_identifier_type.deserialize_aws_json_1_1(
                data["User"]
            )
        )
    else:
        raise DeserializationError("AdminDisableProviderForUserRequest.user required")
    return out
