"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeManagedLoginBrandingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.managed_login_branding_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DescribeManagedLoginBrandingRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the managed login branding style that you want to get information about.</p>"""
    managed_login_branding_id: "capo_cognito_identity_provider.types.managed_login_branding_id_type.ManagedLoginBrandingIdType"
    """<p>The ID of the managed login branding style that you want to get more information about.</p>"""
    return_merged_resources: (
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>When <code>true</code>, returns values for branding options that are unchanged from Amazon Cognito defaults. When <code>false</code> or when you omit this parameter, returns only values that you customized in your branding style.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeManagedLoginBrandingRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ManagedLoginBrandingId"] = value["managed_login_branding_id"]
    out["ReturnMergedResources"] = value.get("return_merged_resources", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeManagedLoginBrandingRequest:
    out: DescribeManagedLoginBrandingRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DescribeManagedLoginBrandingRequest.user_pool_id required"
        )
    if "ManagedLoginBrandingId" in data:
        out["managed_login_branding_id"] = data["ManagedLoginBrandingId"]
    else:
        raise DeserializationError(
            "DescribeManagedLoginBrandingRequest.managed_login_branding_id required"
        )
    if "ReturnMergedResources" in data:
        out["return_merged_resources"] = data["ReturnMergedResources"]
    else:
        out["return_merged_resources"] = False
    return out
