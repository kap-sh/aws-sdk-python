"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_list_type
    import aws_sdk_cognito_identity_provider.types.mfa_option_list_type
    import aws_sdk_cognito_identity_provider.types.string_type
    import aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type
    import aws_sdk_cognito_identity_provider.types.username_type


class GetUserResponse(TypedDict, closed=True):
    username: "aws_sdk_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you requested.</p>"""
    user_attributes: (
        "aws_sdk_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    )
    """<p>An array of name-value pairs representing user attributes.</p> <p>Custom attributes are prepended with the <code>custom:</code> prefix.</p>"""
    mfa_options: NotRequired[
        "aws_sdk_cognito_identity_provider.types.mfa_option_list_type.MFAOptionListType"
    ]
    """<p> <i>This response parameter is no longer supported.</i> It provides information only about SMS MFA configurations. It doesn't provide information about time-based one-time password (TOTP) software token MFA configurations. To look up information about either type of MFA configuration, use UserMFASettingList instead.</p>"""
    preferred_mfa_setting: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The user's preferred MFA. Users can prefer SMS message, email message, or TOTP MFA.</p>"""
    user_mfa_setting_list: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type.UserMFASettingListType"
    ]
    """<p>The MFA options that are activated for the user. The possible values in this list are <code>SMS_MFA</code>, <code>EMAIL_OTP</code>, and <code>SOFTWARE_TOKEN_MFA</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserResponse) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    import aws_sdk_cognito_identity_provider.types.attribute_list_type

    out["UserAttributes"] = (
        aws_sdk_cognito_identity_provider.types.attribute_list_type.serialize_aws_json_1_1(
            value["user_attributes"]
        )
    )
    if "mfa_options" in value:
        import aws_sdk_cognito_identity_provider.types.mfa_option_list_type

        out["MFAOptions"] = (
            aws_sdk_cognito_identity_provider.types.mfa_option_list_type.serialize_aws_json_1_1(
                value["mfa_options"]
            )
        )
    if "preferred_mfa_setting" in value:
        out["PreferredMfaSetting"] = value["preferred_mfa_setting"]
    if "user_mfa_setting_list" in value:
        import aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type

        out["UserMFASettingList"] = (
            aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type.serialize_aws_json_1_1(
                value["user_mfa_setting_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("GetUserResponse.username required")
    if "UserAttributes" in data:
        import aws_sdk_cognito_identity_provider.types.attribute_list_type

        out["user_attributes"] = (
            aws_sdk_cognito_identity_provider.types.attribute_list_type.deserialize_aws_json_1_1(
                data["UserAttributes"]
            )
        )
    else:
        raise DeserializationError("GetUserResponse.user_attributes required")
    if "MFAOptions" in data:
        import aws_sdk_cognito_identity_provider.types.mfa_option_list_type

        out["mfa_options"] = (
            aws_sdk_cognito_identity_provider.types.mfa_option_list_type.deserialize_aws_json_1_1(
                data["MFAOptions"]
            )
        )
    if "PreferredMfaSetting" in data:
        out["preferred_mfa_setting"] = data["PreferredMfaSetting"]
    if "UserMFASettingList" in data:
        import aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type

        out["user_mfa_setting_list"] = (
            aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type.deserialize_aws_json_1_1(
                data["UserMFASettingList"]
            )
        )
    return out
