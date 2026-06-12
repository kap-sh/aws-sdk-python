"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeIdentityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.provider_name_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class DescribeIdentityProviderRequest(TypedDict):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that has the IdP that you want to describe..</p>"""
    provider_name: (
        "aws_sdk_cognito_identity_provider.types.provider_name_type.ProviderNameType"
    )
    """<p>The name of the IdP that you want to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIdentityProviderRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ProviderName"] = value["provider_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIdentityProviderRequest:
    out: DescribeIdentityProviderRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DescribeIdentityProviderRequest.user_pool_id required"
        )
    if "ProviderName" in data:
        out["provider_name"] = data["ProviderName"]
    else:
        raise DeserializationError(
            "DescribeIdentityProviderRequest.provider_name required"
        )
    return out
