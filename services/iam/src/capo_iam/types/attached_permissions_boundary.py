"""Generated from Smithy shape ``com.amazonaws.iam#AttachedPermissionsBoundary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.permissions_boundary_attachment_type


class AttachedPermissionsBoundary(TypedDict, closed=True):
    permissions_boundary_type: NotRequired[
        "capo_iam.types.permissions_boundary_attachment_type.PermissionsBoundaryAttachmentType"
    ]
    """<p> The permissions boundary usage type that indicates what type of IAM resource is used as the permissions boundary for an entity. This data type can only have a value of <code>Policy</code>.</p>"""
    permissions_boundary_arn: NotRequired["capo_iam.types.arn_type.arnType"]
    """<p> The ARN of the policy used to set the permissions boundary for the user or role.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AttachedPermissionsBoundary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "permissions_boundary_type" in value:
        import capo_iam.types.permissions_boundary_attachment_type

        capo_iam.types.permissions_boundary_attachment_type.serialize_query(
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
        import capo_iam.types.permissions_boundary_attachment_type

        out["permissions_boundary_type"] = (
            capo_iam.types.permissions_boundary_attachment_type.deserialize_query(
                child_permissions_boundary_type
            )
        )
    child_permissions_boundary_arn = el.find("PermissionsBoundaryArn")
    if child_permissions_boundary_arn is not None:
        out["permissions_boundary_arn"] = str(child_permissions_boundary_arn.text or "")
    return out
