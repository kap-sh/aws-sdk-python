"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.security_group_id_list
    import aws_sdk_wickr.types.sensitive_string
    import aws_sdk_wickr.types.user_id


class UpdateUserResponse(TypedDict):
    user_id: "aws_sdk_wickr.types.user_id.UserId"
    """<p>The unique identifier of the updated user.</p>"""
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the network where the user was updated.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_wickr.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The list of security group IDs to which the user now belongs after the update.</p>"""
    first_name: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The updated first name of the user.</p>"""
    last_name: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The updated last name of the user.</p>"""
    middle_name: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The middle name of the user (currently not used).</p>"""
    suspended: "bool"
    """<p>Indicates whether the user is suspended after the update.</p>"""
    modified: NotRequired["int"]
    """<p>The timestamp when the user was last modified, specified in epoch seconds.</p>"""
    status: NotRequired["int"]
    """<p>The user's status after the update.</p>"""
    invite_code: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The updated invite code for the user, if applicable.</p>"""
    invite_expiration: NotRequired["int"]
    """<p>The expiration time of the user's invite code, specified in epoch seconds.</p>"""
    code_validation: NotRequired["bool"]
    """<p>Indicates whether the user can be verified through a custom invite code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserResponse) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    out["networkId"] = value["network_id"]
    if "security_group_ids" in value:
        import aws_sdk_wickr.types.security_group_id_list

        out["securityGroupIds"] = (
            aws_sdk_wickr.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "middle_name" in value:
        out["middleName"] = value["middle_name"]
    out["suspended"] = value["suspended"]
    if "modified" in value:
        out["modified"] = value["modified"]
    if "status" in value:
        out["status"] = value["status"]
    if "invite_code" in value:
        out["inviteCode"] = value["invite_code"]
    if "invite_expiration" in value:
        out["inviteExpiration"] = value["invite_expiration"]
    if "code_validation" in value:
        out["codeValidation"] = value["code_validation"]
    return out


def deserialize_json(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UpdateUserResponse.user_id required")
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    else:
        raise DeserializationError("UpdateUserResponse.network_id required")
    if "securityGroupIds" in data:
        import aws_sdk_wickr.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_wickr.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    if "middleName" in data:
        out["middle_name"] = data["middleName"]
    if "suspended" in data:
        out["suspended"] = data["suspended"]
    else:
        raise DeserializationError("UpdateUserResponse.suspended required")
    if "modified" in data:
        out["modified"] = data["modified"]
    if "status" in data:
        out["status"] = data["status"]
    if "inviteCode" in data:
        out["invite_code"] = data["inviteCode"]
    if "inviteExpiration" in data:
        out["invite_expiration"] = data["inviteExpiration"]
    if "codeValidation" in data:
        out["code_validation"] = data["codeValidation"]
    return out
