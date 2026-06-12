"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminGetUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_list_type
    import aws_sdk_cognito_identity_provider.types.boolean_type
    import aws_sdk_cognito_identity_provider.types.date_type
    import aws_sdk_cognito_identity_provider.types.mfa_option_list_type
    import aws_sdk_cognito_identity_provider.types.string_type
    import aws_sdk_cognito_identity_provider.types.user_mfa_setting_list_type
    import aws_sdk_cognito_identity_provider.types.user_status_type
    import aws_sdk_cognito_identity_provider.types.username_type


class AdminGetUserResponse(TypedDict):
    username: "aws_sdk_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The username of the user that you requested.</p>"""
    user_attributes: NotRequired[
        "aws_sdk_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    ]
    """<p>An array of name-value pairs of user attributes and their values, for example <code>\"email\": \"testuser@example.com\"</code>.</p>"""
    user_create_date: NotRequired[
        "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    user_last_modified_date: NotRequired[
        "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    enabled: "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Indicates whether the user is activated for sign-in.</p>"""
    user_status: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_status_type.UserStatusType"
    ]
    """<p>The user's status. Can be one of the following:</p> <ul> <li> <p>UNCONFIRMED - User has been created but not confirmed.</p> </li> <li> <p>CONFIRMED - User has been confirmed.</p> </li> <li> <p>UNKNOWN - User status isn't known.</p> </li> <li> <p>RESET_REQUIRED - User is confirmed, but the user must request a code and reset their password before they can sign in.</p> </li> <li> <p>FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change their password to a new value before doing anything else. </p> </li> <li> <p>EXTERNAL_PROVIDER - The user signed in with a third-party identity provider.</p> </li> </ul>"""
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
def serialize_aws_json_1_1(value: AdminGetUserResponse) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    if "user_attributes" in value:
        import aws_sdk_cognito_identity_provider.types.attribute_list_type

        out["UserAttributes"] = (
            aws_sdk_cognito_identity_provider.types.attribute_list_type.serialize_aws_json_1_1(
                value["user_attributes"]
            )
        )
    if "user_create_date" in value:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["UserCreateDate"] = (
            aws_sdk_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["user_create_date"]
            )
        )
    if "user_last_modified_date" in value:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["UserLastModifiedDate"] = (
            aws_sdk_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["user_last_modified_date"]
            )
        )
    out["Enabled"] = value.get("enabled", False)
    if "user_status" in value:
        import aws_sdk_cognito_identity_provider.types.user_status_type

        out["UserStatus"] = (
            aws_sdk_cognito_identity_provider.types.user_status_type.serialize_aws_json_1_1(
                value["user_status"]
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


def deserialize_aws_json_1_1(data: dict) -> AdminGetUserResponse:
    out: AdminGetUserResponse = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminGetUserResponse.username required")
    if "UserAttributes" in data:
        import aws_sdk_cognito_identity_provider.types.attribute_list_type

        out["user_attributes"] = (
            aws_sdk_cognito_identity_provider.types.attribute_list_type.deserialize_aws_json_1_1(
                data["UserAttributes"]
            )
        )
    if "UserCreateDate" in data:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["user_create_date"] = (
            aws_sdk_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["UserCreateDate"]
            )
        )
    if "UserLastModifiedDate" in data:
        import aws_sdk_cognito_identity_provider.types.date_type

        out["user_last_modified_date"] = (
            aws_sdk_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["UserLastModifiedDate"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if "UserStatus" in data:
        import aws_sdk_cognito_identity_provider.types.user_status_type

        out["user_status"] = (
            aws_sdk_cognito_identity_provider.types.user_status_type.deserialize_aws_json_1_1(
                data["UserStatus"]
            )
        )
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
