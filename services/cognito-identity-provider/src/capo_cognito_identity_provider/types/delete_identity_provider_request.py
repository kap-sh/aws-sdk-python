"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteIdentityProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.provider_name_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DeleteIdentityProviderRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to delete the identity provider.</p>"""
    provider_name: (
        "capo_cognito_identity_provider.types.provider_name_type.ProviderNameType"
    )
    """<p>The name of the IdP that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIdentityProviderRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ProviderName"] = value["provider_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIdentityProviderRequest:
    out: DeleteIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DeleteIdentityProviderRequest.user_pool_id required"
        )
    if "ProviderName" in data:
        out["provider_name"] = data["ProviderName"]
    else:
        raise DeserializationError(
            "DeleteIdentityProviderRequest.provider_name required"
        )
    return out
