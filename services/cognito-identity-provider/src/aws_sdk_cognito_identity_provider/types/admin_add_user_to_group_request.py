"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminAddUserToGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.group_name_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type
    import aws_sdk_cognito_identity_provider.types.username_type


class AdminAddUserToGroupRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the group that you want to add the user to.</p>"""
    username: "aws_sdk_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    group_name: "aws_sdk_cognito_identity_provider.types.group_name_type.GroupNameType"
    """<p>The name of the group that you want to add your user to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminAddUserToGroupRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    out["GroupName"] = value["group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminAddUserToGroupRequest:
    out: AdminAddUserToGroupRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("AdminAddUserToGroupRequest.user_pool_id required")
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminAddUserToGroupRequest.username required")
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    else:
        raise DeserializationError("AdminAddUserToGroupRequest.group_name required")
    return out
