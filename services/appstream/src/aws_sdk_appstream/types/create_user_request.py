"""Generated from Smithy shape ``com.amazonaws.appstream#CreateUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.authentication_type
    import aws_sdk_appstream.types.message_action
    import aws_sdk_appstream.types.user_attribute_value
    import aws_sdk_appstream.types.username


class CreateUserRequest(TypedDict):
    user_name: NotRequired["aws_sdk_appstream.types.username.Username"]
    r"""<p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a \"user does not exist\" error message displays.</p> </note>"""
    message_action: NotRequired["aws_sdk_appstream.types.message_action.MessageAction"]
    """<p>The action to take for the welcome email that is sent to a user after the user is created in the user pool. If you specify SUPPRESS, no email is sent. If you specify RESEND, do not specify the first name or last name of the user. If the value is null, the email is sent. </p> <note> <p>The temporary password in the welcome email is valid for only 7 days. If users don’t set their passwords within 7 days, you must send them a new welcome email.</p> </note>"""
    first_name: NotRequired[
        "aws_sdk_appstream.types.user_attribute_value.UserAttributeValue"
    ]
    """<p>The first name, or given name, of the user.</p>"""
    last_name: NotRequired[
        "aws_sdk_appstream.types.user_attribute_value.UserAttributeValue"
    ]
    """<p>The last name, or surname, of the user.</p>"""
    authentication_type: NotRequired[
        "aws_sdk_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type for the user. You must specify USERPOOL. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserRequest) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "message_action" in value:
        import aws_sdk_appstream.types.message_action

        out["MessageAction"] = (
            aws_sdk_appstream.types.message_action.serialize_aws_json_1_1(
                value["message_action"]
            )
        )
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "authentication_type" in value:
        import aws_sdk_appstream.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "MessageAction" in data:
        import aws_sdk_appstream.types.message_action

        out["message_action"] = (
            aws_sdk_appstream.types.message_action.deserialize_aws_json_1_1(
                data["MessageAction"]
            )
        )
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "AuthenticationType" in data:
        import aws_sdk_appstream.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    return out
