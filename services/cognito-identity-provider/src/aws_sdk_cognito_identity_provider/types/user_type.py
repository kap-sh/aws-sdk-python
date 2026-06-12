"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_list_type
    import aws_sdk_cognito_identity_provider.types.boolean_type
    import aws_sdk_cognito_identity_provider.types.date_type
    import aws_sdk_cognito_identity_provider.types.mfa_option_list_type
    import aws_sdk_cognito_identity_provider.types.user_status_type
    import aws_sdk_cognito_identity_provider.types.username_type


class UserType(TypedDict):
    username: NotRequired[
        "aws_sdk_cognito_identity_provider.types.username_type.UsernameType"
    ]
    """<p>The user's username.</p>"""
    attributes: NotRequired[
        "aws_sdk_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    ]
    """<p>Names and values of a user's attributes, for example <code>email</code>.</p>"""
    user_create_date: NotRequired[
        "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    user_last_modified_date: NotRequired[
        "aws_sdk_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    enabled: "aws_sdk_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Indicates whether the user's account is enabled or disabled.</p>"""
    user_status: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_status_type.UserStatusType"
    ]
    """<p>The user status. This can be one of the following:</p> <ul> <li> <p> <code>UNCONFIRMED</code>: User has been created but not confirmed.</p> </li> <li> <p> <code>CONFIRMED</code>: User has been confirmed.</p> </li> <li> <p> <code>EXTERNAL_PROVIDER</code>: User signed in with a third-party IdP.</p> </li> <li> <p> <code>RESET_REQUIRED</code>: User is confirmed, but the user must request a code and reset their password before they can sign in.</p> </li> <li> <p> <code>FORCE_CHANGE_PASSWORD</code>: The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change their password to a new value before doing anything else. </p> </li> </ul> <p>The statuses <code>ARCHIVED</code>, <code>UNKNOWN</code>, and <code>COMPROMISED</code> are no longer used.</p>"""
    mfa_options: NotRequired[
        "aws_sdk_cognito_identity_provider.types.mfa_option_list_type.MFAOptionListType"
    ]
    """<p>The user's MFA configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserType) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "attributes" in value:
        import aws_sdk_cognito_identity_provider.types.attribute_list_type

        out["Attributes"] = (
            aws_sdk_cognito_identity_provider.types.attribute_list_type.serialize_aws_json_1_1(
                value["attributes"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UserType:
    out: UserType = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    if "Attributes" in data:
        import aws_sdk_cognito_identity_provider.types.attribute_list_type

        out["attributes"] = (
            aws_sdk_cognito_identity_provider.types.attribute_list_type.deserialize_aws_json_1_1(
                data["Attributes"]
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
    return out
