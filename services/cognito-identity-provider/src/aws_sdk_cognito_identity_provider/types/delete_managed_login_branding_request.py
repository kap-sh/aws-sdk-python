"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteManagedLoginBrandingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.managed_login_branding_id_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class DeleteManagedLoginBrandingRequest(TypedDict):
    managed_login_branding_id: "aws_sdk_cognito_identity_provider.types.managed_login_branding_id_type.ManagedLoginBrandingIdType"
    """<p>The ID of the managed login branding style that you want to delete.</p>"""
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the managed login branding style that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteManagedLoginBrandingRequest) -> dict:
    out: dict = {}
    out["ManagedLoginBrandingId"] = value["managed_login_branding_id"]
    out["UserPoolId"] = value["user_pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteManagedLoginBrandingRequest:
    out: DeleteManagedLoginBrandingRequest = {}  # type: ignore[typeddict-item]
    if "ManagedLoginBrandingId" in data:
        out["managed_login_branding_id"] = data["ManagedLoginBrandingId"]
    else:
        raise DeserializationError(
            "DeleteManagedLoginBrandingRequest.managed_login_branding_id required"
        )
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DeleteManagedLoginBrandingRequest.user_pool_id required"
        )
    return out
