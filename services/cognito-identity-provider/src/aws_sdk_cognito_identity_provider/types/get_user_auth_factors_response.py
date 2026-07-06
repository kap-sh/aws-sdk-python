"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUserAuthFactorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.configured_user_auth_factors_list_type
    import aws_sdk_cognito_identity_provider.types.string_type
    import aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type
    import aws_sdk_cognito_identity_provider.types.username_type


class GetUserAuthFactorsResponse(TypedDict, closed=True):
    username: "aws_sdk_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user who is eligible for the authentication factors in the response.</p>"""
    preferred_mfa_setting: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The challenge method that Amazon Cognito returns to the user in response to sign-in requests. Users can prefer SMS message, email message, or TOTP MFA.</p>"""
    user_mfa_setting_list: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type.UserMFASettingListType"
    ]
    """<p>The MFA options that are activated for the user. The possible values in this list are <code>SMS_MFA</code>, <code>EMAIL_OTP</code>, and <code>SOFTWARE_TOKEN_MFA</code>.</p>"""
    configured_user_auth_factors: NotRequired[
        "aws_sdk_cognito_identity_provider.types.configured_user_auth_factors_list_type.ConfiguredUserAuthFactorsListType"
    ]
    r"""<p>The authentication types that are available to the user with <code>USER_AUTH</code> sign-in, for example <code>[\"PASSWORD\", \"WEB_AUTHN\"]</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserAuthFactorsResponse) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    if "preferred_mfa_setting" in value:
        out["PreferredMfaSetting"] = value["preferred_mfa_setting"]
    if "user_mfa_setting_list" in value:
        import aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type

        out["UserMFASettingList"] = (
            aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type.serialize_aws_json_1_1(
                value["user_mfa_setting_list"]
            )
        )
    if "configured_user_auth_factors" in value:
        import aws_sdk_cognito_identity_provider.types.configured_user_auth_factors_list_type

        out["ConfiguredUserAuthFactors"] = (
            aws_sdk_cognito_identity_provider.types.configured_user_auth_factors_list_type.serialize_aws_json_1_1(
                value["configured_user_auth_factors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserAuthFactorsResponse:
    out: GetUserAuthFactorsResponse = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("GetUserAuthFactorsResponse.username required")
    if "PreferredMfaSetting" in data:
        out["preferred_mfa_setting"] = data["PreferredMfaSetting"]
    if "UserMFASettingList" in data:
        import aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type

        out["user_mfa_setting_list"] = (
            aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type.deserialize_aws_json_1_1(
                data["UserMFASettingList"]
            )
        )
    if "ConfiguredUserAuthFactors" in data:
        import aws_sdk_cognito_identity_provider.types.configured_user_auth_factors_list_type

        out["configured_user_auth_factors"] = (
            aws_sdk_cognito_identity_provider.types.configured_user_auth_factors_list_type.deserialize_aws_json_1_1(
                data["ConfiguredUserAuthFactors"]
            )
        )
    return out
