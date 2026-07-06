"""Generated from Smithy shape ``com.amazonaws.finspacedata#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.api_access
    import aws_sdk_finspace_data.types.client_token
    import aws_sdk_finspace_data.types.first_name
    import aws_sdk_finspace_data.types.last_name
    import aws_sdk_finspace_data.types.role_arn
    import aws_sdk_finspace_data.types.user_id
    import aws_sdk_finspace_data.types.user_type


class UpdateUserRequest(TypedDict, closed=True):
    user_id: "aws_sdk_finspace_data.types.user_id.UserId"
    """<p>The unique identifier for the user that you want to update.</p>"""
    type: NotRequired["aws_sdk_finspace_data.types.user_type.UserType"]
    """<p>The option to indicate the type of user.</p> <ul> <li> <p> <code>SUPER_USER</code>– A user with permission to all the functionality and data in FinSpace.</p> </li> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>"""
    first_name: NotRequired["aws_sdk_finspace_data.types.first_name.FirstName"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["aws_sdk_finspace_data.types.last_name.LastName"]
    """<p>The last name of the user.</p>"""
    api_access: NotRequired["aws_sdk_finspace_data.types.api_access.ApiAccess"]
    """<p>The option to indicate whether the user can use the <code>GetProgrammaticAccessCredentials</code> API to obtain credentials that can then be used to access other FinSpace Data API operations.</p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the APIs.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any APIs.</p> </li> </ul>"""
    api_access_principal_arn: NotRequired[
        "aws_sdk_finspace_data.types.role_arn.RoleArn"
    ]
    """<p>The ARN identifier of an AWS user or role that is allowed to call the <code>GetProgrammaticAccessCredentials</code> API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.</p>"""
    client_token: NotRequired["aws_sdk_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_finspace_data.types.user_type

        out["type"] = aws_sdk_finspace_data.types.user_type.serialize_json(
            value["type"]
        )
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "api_access" in value:
        import aws_sdk_finspace_data.types.api_access

        out["apiAccess"] = aws_sdk_finspace_data.types.api_access.serialize_json(
            value["api_access"]
        )
    if "api_access_principal_arn" in value:
        out["apiAccessPrincipalArn"] = value["api_access_principal_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_finspace_data.types.user_type

        out["type"] = aws_sdk_finspace_data.types.user_type.deserialize_json(
            data["type"]
        )
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    if "apiAccess" in data:
        import aws_sdk_finspace_data.types.api_access

        out["api_access"] = aws_sdk_finspace_data.types.api_access.deserialize_json(
            data["apiAccess"]
        )
    if "apiAccessPrincipalArn" in data:
        out["api_access_principal_arn"] = data["apiAccessPrincipalArn"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
