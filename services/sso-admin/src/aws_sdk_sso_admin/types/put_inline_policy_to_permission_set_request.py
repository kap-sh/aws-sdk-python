"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutInlinePolicyToPermissionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.permission_set_arn
    import aws_sdk_sso_admin.types.permission_set_policy_document


class PutInlinePolicyToPermissionSetRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    r"""<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the permission set.</p>"""
    inline_policy: "aws_sdk_sso_admin.types.permission_set_policy_document.PermissionSetPolicyDocument"
    """<p>The inline policy to attach to a <a>PermissionSet</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutInlinePolicyToPermissionSetRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    out["InlinePolicy"] = value["inline_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutInlinePolicyToPermissionSetRequest:
    out: PutInlinePolicyToPermissionSetRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "PutInlinePolicyToPermissionSetRequest.instance_arn required"
        )
    if "PermissionSetArn" in data:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "PutInlinePolicyToPermissionSetRequest.permission_set_arn required"
        )
    if "InlinePolicy" in data:
        out["inline_policy"] = data["InlinePolicy"]
    else:
        raise DeserializationError(
            "PutInlinePolicyToPermissionSetRequest.inline_policy required"
        )
    return out
