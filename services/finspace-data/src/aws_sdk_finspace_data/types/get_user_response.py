"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.api_access
    import aws_sdk_finspace_data.types.email
    import aws_sdk_finspace_data.types.first_name
    import aws_sdk_finspace_data.types.last_name
    import aws_sdk_finspace_data.types.role_arn
    import aws_sdk_finspace_data.types.timestamp_epoch
    import aws_sdk_finspace_data.types.user_id
    import aws_sdk_finspace_data.types.user_status
    import aws_sdk_finspace_data.types.user_type


class GetUserResponse(TypedDict, closed=True):
    user_id: NotRequired["aws_sdk_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier for the user that is retrieved.</p>"""
    status: NotRequired["aws_sdk_finspace_data.types.user_status.UserStatus"]
    """<p>The current status of the user. </p> <ul> <li> <p> <code>CREATING</code> – The creation is in progress.</p> </li> <li> <p> <code>ENABLED</code> – The user is created and is currently active.</p> </li> <li> <p> <code>DISABLED</code> – The user is currently inactive.</p> </li> </ul>"""
    first_name: NotRequired["aws_sdk_finspace_data.types.first_name.FirstName"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["aws_sdk_finspace_data.types.last_name.LastName"]
    """<p>The last name of the user.</p>"""
    email_address: NotRequired["aws_sdk_finspace_data.types.email.Email"]
    """<p>The email address that is associated with the user.</p>"""
    type: NotRequired["aws_sdk_finspace_data.types.user_type.UserType"]
    """<p>Indicates the type of user. </p> <ul> <li> <p> <code>SUPER_USER</code> – A user with permission to all the functionality and data in FinSpace.</p> </li> </ul> <ul> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>"""
    api_access: NotRequired["aws_sdk_finspace_data.types.api_access.ApiAccess"]
    """<p>Indicates whether the user can use the <code>GetProgrammaticAccessCredentials</code> API to obtain credentials that can then be used to access other FinSpace Data API operations. </p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the APIs.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any APIs.</p> </li> </ul>"""
    api_access_principal_arn: NotRequired[
        "aws_sdk_finspace_data.types.role_arn.RoleArn"
    ]
    """<p>The ARN identifier of an AWS user or role that is allowed to call the <code>GetProgrammaticAccessCredentials</code> API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.</p>"""
    create_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The timestamp at which the user was created in FinSpace. The value is determined as epoch time in milliseconds. </p>"""
    last_enabled_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time the user was activated. The value is determined as epoch time in milliseconds.</p>"""
    last_disabled_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time the user was deactivated. The value is determined as epoch time in milliseconds.</p>"""
    last_modified_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time the user details were updated. The value is determined as epoch time in milliseconds.</p>"""
    last_login_time: "aws_sdk_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time that the user logged into their account. The value is determined as epoch time in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "status" in value:
        import aws_sdk_finspace_data.types.user_status

        out["status"] = aws_sdk_finspace_data.types.user_status.serialize_json(
            value["status"]
        )
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "type" in value:
        import aws_sdk_finspace_data.types.user_type

        out["type"] = aws_sdk_finspace_data.types.user_type.serialize_json(
            value["type"]
        )
    if "api_access" in value:
        import aws_sdk_finspace_data.types.api_access

        out["apiAccess"] = aws_sdk_finspace_data.types.api_access.serialize_json(
            value["api_access"]
        )
    if "api_access_principal_arn" in value:
        out["apiAccessPrincipalArn"] = value["api_access_principal_arn"]
    out["createTime"] = value.get("create_time", 0)
    out["lastEnabledTime"] = value.get("last_enabled_time", 0)
    out["lastDisabledTime"] = value.get("last_disabled_time", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    out["lastLoginTime"] = value.get("last_login_time", 0)
    return out


def deserialize_json(data: dict) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "status" in data:
        import aws_sdk_finspace_data.types.user_status

        out["status"] = aws_sdk_finspace_data.types.user_status.deserialize_json(
            data["status"]
        )
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    if "emailAddress" in data:
        out["email_address"] = data["emailAddress"]
    if "type" in data:
        import aws_sdk_finspace_data.types.user_type

        out["type"] = aws_sdk_finspace_data.types.user_type.deserialize_json(
            data["type"]
        )
    if "apiAccess" in data:
        import aws_sdk_finspace_data.types.api_access

        out["api_access"] = aws_sdk_finspace_data.types.api_access.deserialize_json(
            data["apiAccess"]
        )
    if "apiAccessPrincipalArn" in data:
        out["api_access_principal_arn"] = data["apiAccessPrincipalArn"]
    if "createTime" in data:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = 0
    if "lastEnabledTime" in data:
        out["last_enabled_time"] = data["lastEnabledTime"]
    else:
        out["last_enabled_time"] = 0
    if "lastDisabledTime" in data:
        out["last_disabled_time"] = data["lastDisabledTime"]
    else:
        out["last_disabled_time"] = 0
    if "lastModifiedTime" in data:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if "lastLoginTime" in data:
        out["last_login_time"] = data["lastLoginTime"]
    else:
        out["last_login_time"] = 0
    return out
