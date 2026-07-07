"""Generated from Smithy shape ``com.amazonaws.wickr#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.security_group_id_list
    import aws_sdk_wickr.types.sensitive_string
    import aws_sdk_wickr.types.user_id


class User(TypedDict, closed=True):
    user_id: NotRequired["aws_sdk_wickr.types.user_id.UserId"]
    """<p>The unique identifier for the user within the network.</p>"""
    first_name: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The last name of the user.</p>"""
    username: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The email address or username of the user. For bots, this must end in 'bot'.</p>"""
    security_groups: NotRequired[
        "aws_sdk_wickr.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>A list of security group IDs to which the user is assigned, determining their permissions and feature access.</p>"""
    is_admin: NotRequired["bool"]
    """<p>Indicates whether the user has administrator privileges in the network.</p>"""
    suspended: NotRequired["bool"]
    """<p>Indicates whether the user is currently suspended and unable to access the network.</p>"""
    status: NotRequired["int"]
    """<p>The current status of the user (1 for pending invitation, 2 for active).</p>"""
    otp_enabled: NotRequired["bool"]
    """<p>Indicates whether one-time password (OTP) authentication is enabled for the user.</p>"""
    scim_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The SCIM (System for Cross-domain Identity Management) identifier for the user, used for identity synchronization. Currently not used.</p>"""
    type: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The descriptive type of the user account (e.g., 'user').</p>"""
    cell: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The phone number minus country code, used for cloud deployments.</p>"""
    country_code: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The country code for the user's phone number, used for cloud deployments.</p>"""
    challenge_failures: NotRequired["int"]
    """<p>The number of failed password attempts for enterprise deployments, used for account lockout policies.</p>"""
    is_invite_expired: NotRequired["bool"]
    """<p>Indicates whether the user's email invitation code has expired, applicable to cloud deployments.</p>"""
    is_user: NotRequired["bool"]
    """<p>Indicates whether this account is a user (as opposed to a bot or other account type).</p>"""
    invite_code: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The invitation code for this user, used during registration to join the network.</p>"""
    code_validation: NotRequired["bool"]
    """<p>Indicates whether the user can be verified through a custom invite code.</p>"""
    uname: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The unique identifier for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "username" in value:
        out["username"] = value["username"]
    if "security_groups" in value:
        import aws_sdk_wickr.types.security_group_id_list

        out["securityGroups"] = (
            aws_sdk_wickr.types.security_group_id_list.serialize_json(
                value["security_groups"]
            )
        )
    if "is_admin" in value:
        out["isAdmin"] = value["is_admin"]
    if "suspended" in value:
        out["suspended"] = value["suspended"]
    if "status" in value:
        out["status"] = value["status"]
    if "otp_enabled" in value:
        out["otpEnabled"] = value["otp_enabled"]
    if "scim_id" in value:
        out["scimId"] = value["scim_id"]
    if "type" in value:
        out["type"] = value["type"]
    if "cell" in value:
        out["cell"] = value["cell"]
    if "country_code" in value:
        out["countryCode"] = value["country_code"]
    if "challenge_failures" in value:
        out["challengeFailures"] = value["challenge_failures"]
    if "is_invite_expired" in value:
        out["isInviteExpired"] = value["is_invite_expired"]
    if "is_user" in value:
        out["isUser"] = value["is_user"]
    if "invite_code" in value:
        out["inviteCode"] = value["invite_code"]
    if "code_validation" in value:
        out["codeValidation"] = value["code_validation"]
    if "uname" in value:
        out["uname"] = value["uname"]
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "firstName" in data:
        out["first_name"] = data["firstName"]
    if "lastName" in data:
        out["last_name"] = data["lastName"]
    if "username" in data:
        out["username"] = data["username"]
    if "securityGroups" in data:
        import aws_sdk_wickr.types.security_group_id_list

        out["security_groups"] = (
            aws_sdk_wickr.types.security_group_id_list.deserialize_json(
                data["securityGroups"]
            )
        )
    if "isAdmin" in data:
        out["is_admin"] = data["isAdmin"]
    if "suspended" in data:
        out["suspended"] = data["suspended"]
    if "status" in data:
        out["status"] = data["status"]
    if "otpEnabled" in data:
        out["otp_enabled"] = data["otpEnabled"]
    if "scimId" in data:
        out["scim_id"] = data["scimId"]
    if "type" in data:
        out["type"] = data["type"]
    if "cell" in data:
        out["cell"] = data["cell"]
    if "countryCode" in data:
        out["country_code"] = data["countryCode"]
    if "challengeFailures" in data:
        out["challenge_failures"] = data["challengeFailures"]
    if "isInviteExpired" in data:
        out["is_invite_expired"] = data["isInviteExpired"]
    if "isUser" in data:
        out["is_user"] = data["isUser"]
    if "inviteCode" in data:
        out["invite_code"] = data["inviteCode"]
    if "codeValidation" in data:
        out["code_validation"] = data["codeValidation"]
    if "uname" in data:
        out["uname"] = data["uname"]
    return out
