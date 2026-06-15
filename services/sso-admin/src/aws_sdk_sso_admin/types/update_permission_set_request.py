"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UpdatePermissionSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.duration
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.permission_set_arn
    import aws_sdk_sso_admin.types.permission_set_description
    import aws_sdk_sso_admin.types.relay_state


class UpdatePermissionSetRequest(TypedDict):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    r"""<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the permission set.</p>"""
    description: NotRequired[
        "aws_sdk_sso_admin.types.permission_set_description.PermissionSetDescription"
    ]
    """<p>The description of the <a>PermissionSet</a>.</p>"""
    session_duration: NotRequired["aws_sdk_sso_admin.types.duration.Duration"]
    """<p>The length of time that the application user sessions are valid for in the ISO-8601 standard.</p>"""
    relay_state: NotRequired["aws_sdk_sso_admin.types.relay_state.RelayState"]
    """<p>Used to redirect users within the application during the federation authentication process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePermissionSetRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "session_duration" in value:
        out["SessionDuration"] = value["session_duration"]
    if "relay_state" in value:
        out["RelayState"] = value["relay_state"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePermissionSetRequest:
    out: UpdatePermissionSetRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("UpdatePermissionSetRequest.instance_arn required")
    if "PermissionSetArn" in data:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "UpdatePermissionSetRequest.permission_set_arn required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "SessionDuration" in data:
        out["session_duration"] = data["SessionDuration"]
    if "RelayState" in data:
        out["relay_state"] = data["RelayState"]
    return out
