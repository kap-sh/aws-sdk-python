"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#UpdateProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.managed_policy_list
    import aws_sdk_rolesanywhere.types.resource_name
    import aws_sdk_rolesanywhere.types.role_arn_list
    import aws_sdk_rolesanywhere.types.uuid


class UpdateProfileRequest(TypedDict):
    profile_id: "aws_sdk_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the profile.</p>"""
    name: NotRequired["aws_sdk_rolesanywhere.types.resource_name.ResourceName"]
    """<p>The name of the profile.</p>"""
    session_policy: NotRequired["str"]
    """<p>A session policy that applies to the trust boundary of the vended session credentials. </p>"""
    role_arns: NotRequired["aws_sdk_rolesanywhere.types.role_arn_list.RoleArnList"]
    """<p>A list of IAM roles that this profile can assume in a temporary credential request.</p>"""
    managed_policy_arns: NotRequired[
        "aws_sdk_rolesanywhere.types.managed_policy_list.ManagedPolicyList"
    ]
    """<p>A list of managed policy ARNs that apply to the vended session credentials. </p>"""
    duration_seconds: NotRequired["int"]
    r"""<p> Used to determine how long sessions vended using this profile are valid for. See the <code>Expiration</code> section of the <a href=\"https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object\">CreateSession API documentation</a> page for more details. In requests, if this value is not provided, the default value will be 3600. </p>"""
    accept_role_session_name: NotRequired["bool"]
    """<p>Used to determine if a custom role session name will be accepted in a temporary credential request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "session_policy" in value:
        out["sessionPolicy"] = value["session_policy"]
    if "role_arns" in value:
        import aws_sdk_rolesanywhere.types.role_arn_list

        out["roleArns"] = aws_sdk_rolesanywhere.types.role_arn_list.serialize_json(
            value["role_arns"]
        )
    if "managed_policy_arns" in value:
        import aws_sdk_rolesanywhere.types.managed_policy_list

        out["managedPolicyArns"] = (
            aws_sdk_rolesanywhere.types.managed_policy_list.serialize_json(
                value["managed_policy_arns"]
            )
        )
    if "duration_seconds" in value:
        out["durationSeconds"] = value["duration_seconds"]
    if "accept_role_session_name" in value:
        out["acceptRoleSessionName"] = value["accept_role_session_name"]
    return out


def deserialize_json(data: dict) -> UpdateProfileRequest:
    out: UpdateProfileRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "sessionPolicy" in data:
        out["session_policy"] = data["sessionPolicy"]
    if "roleArns" in data:
        import aws_sdk_rolesanywhere.types.role_arn_list

        out["role_arns"] = aws_sdk_rolesanywhere.types.role_arn_list.deserialize_json(
            data["roleArns"]
        )
    if "managedPolicyArns" in data:
        import aws_sdk_rolesanywhere.types.managed_policy_list

        out["managed_policy_arns"] = (
            aws_sdk_rolesanywhere.types.managed_policy_list.deserialize_json(
                data["managedPolicyArns"]
            )
        )
    if "durationSeconds" in data:
        out["duration_seconds"] = data["durationSeconds"]
    if "acceptRoleSessionName" in data:
        out["accept_role_session_name"] = data["acceptRoleSessionName"]
    return out
