"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminSetUserSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.mfa_option_list_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type
    import aws_sdk_cognito_identity_provider.types.username_type


class AdminSetUserSettingsRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the user whose options you're setting.</p>"""
    username: "aws_sdk_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    mfa_options: (
        "aws_sdk_cognito_identity_provider.types.mfa_option_list_type.MFAOptionListType"
    )
    """<p>You can use this parameter only to set an SMS configuration that uses SMS for delivery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminSetUserSettingsRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    import aws_sdk_cognito_identity_provider.types.mfa_option_list_type

    out["MFAOptions"] = (
        aws_sdk_cognito_identity_provider.types.mfa_option_list_type.serialize_aws_json_1_1(
            value["mfa_options"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminSetUserSettingsRequest:
    out: AdminSetUserSettingsRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("AdminSetUserSettingsRequest.user_pool_id required")
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminSetUserSettingsRequest.username required")
    if "MFAOptions" in data:
        import aws_sdk_cognito_identity_provider.types.mfa_option_list_type

        out["mfa_options"] = (
            aws_sdk_cognito_identity_provider.types.mfa_option_list_type.deserialize_aws_json_1_1(
                data["MFAOptions"]
            )
        )
    else:
        raise DeserializationError("AdminSetUserSettingsRequest.mfa_options required")
    return out
