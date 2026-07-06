"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreatePermissionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.duration
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.permission_set_description
    import aws_sdk_sso_admin.types.permission_set_name
    import aws_sdk_sso_admin.types.relay_state
    import aws_sdk_sso_admin.types.tag_list


class CreatePermissionSetRequest(TypedDict, closed=True):
    name: "aws_sdk_sso_admin.types.permission_set_name.PermissionSetName"
    """<p>The name of the <a>PermissionSet</a>.</p>"""
    description: NotRequired[
        "aws_sdk_sso_admin.types.permission_set_description.PermissionSetDescription"
    ]
    """<p>The description of the <a>PermissionSet</a>.</p>"""
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    r"""<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    session_duration: NotRequired["aws_sdk_sso_admin.types.duration.Duration"]
    """<p>The length of time that the application user sessions are valid in the ISO-8601 standard.</p>"""
    relay_state: NotRequired["aws_sdk_sso_admin.types.relay_state.RelayState"]
    """<p>Used to redirect users within the application during the federation authentication process.</p>"""
    tags: NotRequired["aws_sdk_sso_admin.types.tag_list.TagList"]
    """<p>The tags to attach to the new <a>PermissionSet</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePermissionSetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["InstanceArn"] = value["instance_arn"]
    if "session_duration" in value:
        out["SessionDuration"] = value["session_duration"]
    if "relay_state" in value:
        out["RelayState"] = value["relay_state"]
    if "tags" in value:
        import aws_sdk_sso_admin.types.tag_list

        out["Tags"] = aws_sdk_sso_admin.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePermissionSetRequest:
    out: CreatePermissionSetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreatePermissionSetRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError("CreatePermissionSetRequest.instance_arn required")
    if "SessionDuration" in data:
        out["session_duration"] = data["SessionDuration"]
    if "RelayState" in data:
        out["relay_state"] = data["RelayState"]
    if "Tags" in data:
        import aws_sdk_sso_admin.types.tag_list

        out["tags"] = aws_sdk_sso_admin.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
