"""Generated from Smithy shape ``com.amazonaws.appstream#UserStackAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.authentication_type
    import aws_sdk_appstream.types.boolean
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.username


class UserStackAssociation(TypedDict):
    stack_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the stack that is associated with the user.</p>"""
    user_name: NotRequired["aws_sdk_appstream.types.username.Username"]
    """<p>The email address of the user who is associated with the stack.</p> <note> <p>Users' email addresses are case-sensitive.</p> </note>"""
    authentication_type: NotRequired[
        "aws_sdk_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type for the user.</p>"""
    send_email_notification: NotRequired["aws_sdk_appstream.types.boolean.Boolean"]
    """<p>Specifies whether a welcome email is sent to a user after the user is created in the user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStackAssociation) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "authentication_type" in value:
        import aws_sdk_appstream.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    if "send_email_notification" in value:
        out["SendEmailNotification"] = value["send_email_notification"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserStackAssociation:
    out: UserStackAssociation = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "AuthenticationType" in data:
        import aws_sdk_appstream.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    if "SendEmailNotification" in data:
        out["send_email_notification"] = data["SendEmailNotification"]
    return out
