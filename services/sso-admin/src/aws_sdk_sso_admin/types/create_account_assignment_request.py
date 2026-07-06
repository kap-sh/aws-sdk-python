"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateAccountAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.instance_arn
    import aws_sdk_sso_admin.types.permission_set_arn
    import aws_sdk_sso_admin.types.principal_id
    import aws_sdk_sso_admin.types.principal_type
    import aws_sdk_sso_admin.types.target_id
    import aws_sdk_sso_admin.types.target_type


class CreateAccountAssignmentRequest(TypedDict, closed=True):
    instance_arn: "aws_sdk_sso_admin.types.instance_arn.InstanceArn"
    r"""<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href=\"/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    target_id: "aws_sdk_sso_admin.types.target_id.TargetId"
    """<p>TargetID is an Amazon Web Services account identifier, (For example, 123456789012).</p>"""
    target_type: "aws_sdk_sso_admin.types.target_type.TargetType"
    """<p>The entity type for which the assignment will be created.</p>"""
    permission_set_arn: "aws_sdk_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the permission set that the admin wants to grant the principal access to.</p>"""
    principal_type: "aws_sdk_sso_admin.types.principal_type.PrincipalType"
    """<p>The entity type for which the assignment will be created.</p>"""
    principal_id: "aws_sdk_sso_admin.types.principal_id.PrincipalId"
    r"""<p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href=\"/singlesignon/latest/IdentityStoreAPIReference/welcome.html\">IAM Identity Center Identity Store API Reference</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccountAssignmentRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["TargetId"] = value["target_id"]
    import aws_sdk_sso_admin.types.target_type

    out["TargetType"] = aws_sdk_sso_admin.types.target_type.serialize_aws_json_1_1(
        value["target_type"]
    )
    out["PermissionSetArn"] = value["permission_set_arn"]
    import aws_sdk_sso_admin.types.principal_type

    out["PrincipalType"] = (
        aws_sdk_sso_admin.types.principal_type.serialize_aws_json_1_1(
            value["principal_type"]
        )
    )
    out["PrincipalId"] = value["principal_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccountAssignmentRequest:
    out: CreateAccountAssignmentRequest = {}  # type: ignore[typeddict-item]
    if "InstanceArn" in data:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "CreateAccountAssignmentRequest.instance_arn required"
        )
    if "TargetId" in data:
        out["target_id"] = data["TargetId"]
    else:
        raise DeserializationError("CreateAccountAssignmentRequest.target_id required")
    if "TargetType" in data:
        import aws_sdk_sso_admin.types.target_type

        out["target_type"] = (
            aws_sdk_sso_admin.types.target_type.deserialize_aws_json_1_1(
                data["TargetType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccountAssignmentRequest.target_type required"
        )
    if "PermissionSetArn" in data:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "CreateAccountAssignmentRequest.permission_set_arn required"
        )
    if "PrincipalType" in data:
        import aws_sdk_sso_admin.types.principal_type

        out["principal_type"] = (
            aws_sdk_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAccountAssignmentRequest.principal_type required"
        )
    if "PrincipalId" in data:
        out["principal_id"] = data["PrincipalId"]
    else:
        raise DeserializationError(
            "CreateAccountAssignmentRequest.principal_id required"
        )
    return out
