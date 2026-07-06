"""Generated from Smithy shape ``com.amazonaws.appstream#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn
    import aws_sdk_appstream.types.authentication_type
    import aws_sdk_appstream.types.boolean
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.timestamp
    import aws_sdk_appstream.types.user_attribute_value
    import aws_sdk_appstream.types.username


class User(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_appstream.types.arn.Arn"]
    """<p>The ARN of the user.</p>"""
    user_name: NotRequired["aws_sdk_appstream.types.username.Username"]
    """<p>The email address of the user.</p> <note> <p>Users' email addresses are case-sensitive.</p> </note>"""
    enabled: NotRequired["aws_sdk_appstream.types.boolean.Boolean"]
    """<p>Specifies whether the user in the user pool is enabled.</p>"""
    status: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The status of the user in the user pool. The status can be one of the following:</p> <ul> <li> <p>UNCONFIRMED – The user is created but not confirmed.</p> </li> <li> <p>CONFIRMED – The user is confirmed.</p> </li> <li> <p>ARCHIVED – The user is no longer active.</p> </li> <li> <p>COMPROMISED – The user is disabled because of a potential security threat.</p> </li> <li> <p>UNKNOWN – The user status is not known.</p> </li> </ul>"""
    first_name: NotRequired[
        "aws_sdk_appstream.types.user_attribute_value.UserAttributeValue"
    ]
    """<p>The first name, or given name, of the user.</p>"""
    last_name: NotRequired[
        "aws_sdk_appstream.types.user_attribute_value.UserAttributeValue"
    ]
    """<p>The last name, or surname, of the user.</p>"""
    created_time: NotRequired["aws_sdk_appstream.types.timestamp.Timestamp"]
    """<p>The date and time the user was created in the user pool.</p>"""
    authentication_type: NotRequired[
        "aws_sdk_appstream.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type for the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: User) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "status" in value:
        out["Status"] = value["status"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "created_time" in value:
        import aws_sdk_appstream.types.timestamp

        out["CreatedTime"] = aws_sdk_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "authentication_type" in value:
        import aws_sdk_appstream.types.authentication_type

        out["AuthenticationType"] = (
            aws_sdk_appstream.types.authentication_type.serialize_aws_json_1_1(
                value["authentication_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "CreatedTime" in data:
        import aws_sdk_appstream.types.timestamp

        out["created_time"] = (
            aws_sdk_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if "AuthenticationType" in data:
        import aws_sdk_appstream.types.authentication_type

        out["authentication_type"] = (
            aws_sdk_appstream.types.authentication_type.deserialize_aws_json_1_1(
                data["AuthenticationType"]
            )
        )
    return out
