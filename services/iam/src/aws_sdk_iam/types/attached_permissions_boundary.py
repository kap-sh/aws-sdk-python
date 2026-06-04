"""Generated from Smithy shape ``com.amazonaws.iam#AttachedPermissionsBoundary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.permissions_boundary_attachment_type


class AttachedPermissionsBoundary(TypedDict):
    permissions_boundary_type: NotRequired[
        "aws_sdk_iam.types.permissions_boundary_attachment_type.PermissionsBoundaryAttachmentType"
    ]
    """<p> The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of <code>Policy</code>.</p>"""
    permissions_boundary_arn: NotRequired["aws_sdk_iam.types.arn_type.arnType"]
    """<p> The ARN of the policy used to set the permissions boundary for the user or role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachedPermissionsBoundary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "permissions_boundary_type" in value:
        import aws_sdk_iam.types.permissions_boundary_attachment_type

        aws_sdk_iam.types.permissions_boundary_attachment_type.serialize_query(
            value["permissions_boundary_type"],
            pairs,
            f"{prefix}.PermissionsBoundaryType",
        )
    if "permissions_boundary_arn" in value:
        pairs.append(
            (f"{prefix}.PermissionsBoundaryArn", str(value["permissions_boundary_arn"]))
        )


def deserialize_query(el: Element) -> AttachedPermissionsBoundary:
    out: AttachedPermissionsBoundary = {}  # type: ignore[typeddict-item]
    child_permissions_boundary_type = el.find("PermissionsBoundaryType")
    if child_permissions_boundary_type is not None:
        import aws_sdk_iam.types.permissions_boundary_attachment_type

        out["permissions_boundary_type"] = (
            aws_sdk_iam.types.permissions_boundary_attachment_type.deserialize_query(
                child_permissions_boundary_type
            )
        )
    child_permissions_boundary_arn = el.find("PermissionsBoundaryArn")
    if child_permissions_boundary_arn is not None:
        out["permissions_boundary_arn"] = str(child_permissions_boundary_arn.text or "")
    return out
