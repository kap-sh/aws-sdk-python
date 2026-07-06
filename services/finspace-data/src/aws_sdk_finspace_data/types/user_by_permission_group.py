"""Generated from Smithy shape ``com.amazonaws.finspacedata#UserByPermissionGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.api_access
    import aws_sdk_finspace_data.types.email
    import aws_sdk_finspace_data.types.first_name
    import aws_sdk_finspace_data.types.last_name
    import aws_sdk_finspace_data.types.permission_group_membership_status
    import aws_sdk_finspace_data.types.role_arn
    import aws_sdk_finspace_data.types.user_id
    import aws_sdk_finspace_data.types.user_status
    import aws_sdk_finspace_data.types.user_type


class UserByPermissionGroup(TypedDict, closed=True):
    user_id: NotRequired["aws_sdk_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier for the user.</p>"""
    status: NotRequired["aws_sdk_finspace_data.types.user_status.UserStatus"]
    """<p>The current status of the user. </p> <ul> <li> <p> <code>CREATING</code> – The user creation is in progress.</p> </li> <li> <p> <code>ENABLED</code> – The user is created and is currently active.</p> </li> <li> <p> <code>DISABLED</code> – The user is currently inactive.</p> </li> </ul>"""
    first_name: NotRequired["aws_sdk_finspace_data.types.first_name.FirstName"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["aws_sdk_finspace_data.types.last_name.LastName"]
    """<p>The last name of the user.</p>"""
    email_address: NotRequired["aws_sdk_finspace_data.types.email.Email"]
    """<p>The email address of the user. The email address serves as a unique identifier for each user and cannot be changed after it's created.</p>"""
    type: NotRequired["aws_sdk_finspace_data.types.user_type.UserType"]
    """<p> Indicates the type of user.</p> <ul> <li> <p> <code>SUPER_USER</code> – A user with permission to all the functionality and data in FinSpace.</p> </li> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>"""
    api_access: NotRequired["aws_sdk_finspace_data.types.api_access.ApiAccess"]
    """<p>Indicates whether the user can access FinSpace API operations.</p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the API operations.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any API operations.</p> </li> </ul>"""
    api_access_principal_arn: NotRequired[
        "aws_sdk_finspace_data.types.role_arn.RoleArn"
    ]
    """<p>The IAM ARN identifier that is attached to FinSpace API calls.</p>"""
    membership_status: NotRequired[
        "aws_sdk_finspace_data.types.permission_group_membership_status.PermissionGroupMembershipStatus"
    ]
    """<p>Indicates the status of the user within a permission group.</p> <ul> <li> <p> <code>ADDITION_IN_PROGRESS</code> – The user is currently being added to the permission group.</p> </li> <li> <p> <code>ADDITION_SUCCESS</code> – The user is successfully added to the permission group.</p> </li> <li> <p> <code>REMOVAL_IN_PROGRESS</code> – The user is currently being removed from the permission group.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserByPermissionGroup) -> dict:
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
    if "membership_status" in value:
        import aws_sdk_finspace_data.types.permission_group_membership_status

        out["membershipStatus"] = (
            aws_sdk_finspace_data.types.permission_group_membership_status.serialize_json(
                value["membership_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserByPermissionGroup:
    out: UserByPermissionGroup = {}  # type: ignore[typeddict-item]
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
    if "membershipStatus" in data:
        import aws_sdk_finspace_data.types.permission_group_membership_status

        out["membership_status"] = (
            aws_sdk_finspace_data.types.permission_group_membership_status.deserialize_json(
                data["membershipStatus"]
            )
        )
    return out
