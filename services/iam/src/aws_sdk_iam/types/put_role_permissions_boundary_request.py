"""Generated from Smithy shape ``com.amazonaws.iam#PutRolePermissionsBoundaryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.role_name_type


class PutRolePermissionsBoundaryRequest(TypedDict):
    role_name: "aws_sdk_iam.types.role_name_type.roleNameType"
    """<p>The name (friendly name, not ARN) of the IAM role for which you want to set the permissions boundary.</p>"""
    permissions_boundary: "aws_sdk_iam.types.arn_type.arnType"
    """<p>The ARN of the managed policy that is used to set the permissions boundary for the role.</p> <p>A permissions boundary policy defines the maximum permissions that identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity. To learn more, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html\">Permissions boundaries for IAM entities</a> in the <i>IAM User Guide</i>.</p> <p>For more information about policy types, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types\">Policy types </a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutRolePermissionsBoundaryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.RoleName", str(value["role_name"])))
    pairs.append((f"{prefix}.PermissionsBoundary", str(value["permissions_boundary"])))


def deserialize_query(el: Element) -> PutRolePermissionsBoundaryRequest:
    out: PutRolePermissionsBoundaryRequest = {}  # type: ignore[typeddict-item]
    child_role_name = el.find("RoleName")
    if child_role_name is not None:
        out["role_name"] = str(child_role_name.text or "")
    else:
        raise DeserializationError(
            "PutRolePermissionsBoundaryRequest.role_name required"
        )
    child_permissions_boundary = el.find("PermissionsBoundary")
    if child_permissions_boundary is not None:
        out["permissions_boundary"] = str(child_permissions_boundary.text or "")
    else:
        raise DeserializationError(
            "PutRolePermissionsBoundaryRequest.permissions_boundary required"
        )
    return out
