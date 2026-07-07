"""Generated from Smithy shape ``com.amazonaws.wickr#GetUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.security_group_id_list
    import aws_sdk_wickr.types.sensitive_string
    import aws_sdk_wickr.types.user_id


class GetUserResponse(TypedDict, closed=True):
    user_id: "aws_sdk_wickr.types.user_id.UserId"
    """<p>The unique identifier of the user.</p>"""
    first_name: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The last name of the user.</p>"""
    username: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The email address or username of the user.</p>"""
    is_admin: NotRequired["bool"]
    """<p>Indicates whether the user has administrator privileges in the network.</p>"""
    suspended: NotRequired["bool"]
    """<p>Indicates whether the user is currently suspended.</p>"""
    status: NotRequired["int"]
    """<p>The current status of the user (1 for pending, 2 for active).</p>"""
    last_activity: NotRequired["int"]
    """<p>The timestamp of the user's last activity in the network, specified in epoch seconds.</p>"""
    last_login: NotRequired["int"]
    """<p>The timestamp of the user's last login to the network, specified in epoch seconds.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_wickr.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>A list of security group IDs to which the user belongs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserResponse) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "username" in value:
        out["username"] = value["username"]
    if "is_admin" in value:
        out["isAdmin"] = value["is_admin"]
    if "suspended" in value:
        out["suspended"] = value["suspended"]
    if "status" in value:
        out["status"] = value["status"]
    if "last_activity" in value:
        out["lastActivity"] = value["last_activity"]
    if "last_login" in value:
        out["lastLogin"] = value["last_login"]
    if "security_group_ids" in value:
        import aws_sdk_wickr.types.security_group_id_list

        out["securityGroupIds"] = (
            aws_sdk_wickr.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("GetUserResponse.user_id required")
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    if "username" in data:
        out["username"] = data["username"]
    if "isAdmin" in data:
        out["is_admin"] = data["isAdmin"]
    if "suspended" in data:
        out["suspended"] = data["suspended"]
    if "status" in data:
        out["status"] = data["status"]
    if "lastActivity" in data:
        out["last_activity"] = data["lastActivity"]
    if "lastLogin" in data:
        out["last_login"] = data["lastLogin"]
    if "securityGroupIds" in data:
        import aws_sdk_wickr.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_wickr.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
