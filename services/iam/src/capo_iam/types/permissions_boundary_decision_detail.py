"""Generated from Smithy shape ``com.amazonaws.iam#PermissionsBoundaryDecisionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type


class PermissionsBoundaryDecisionDetail(TypedDict, closed=True):
    allowed_by_permissions_boundary: "capo_iam.types.boolean_type.booleanType"
    """<p>Specifies whether an action is allowed by a permissions boundary that is applied to an IAM entity (user or role). A value of <code>true</code> means that the permissions boundary does not deny the action. This means that the policy includes an <code>Allow</code> statement that matches the request. In this case, if an identity-based policy also allows the action, the request is allowed. A value of <code>false</code> means that either the requested action is not allowed (implicitly denied) or that the action is explicitly denied by the permissions boundary. In both of these cases, the action is not allowed, regardless of the identity-based policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PermissionsBoundaryDecisionDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (
            f"{prefix}.AllowedByPermissionsBoundary",
            "true" if value.get("allowed_by_permissions_boundary", False) else "false",
        )
    )


def deserialize_query(el: Element) -> PermissionsBoundaryDecisionDetail:
    out: PermissionsBoundaryDecisionDetail = {}  # type: ignore[typeddict-item]
    child_allowed_by_permissions_boundary = el.find("AllowedByPermissionsBoundary")
    if child_allowed_by_permissions_boundary is not None:
        out["allowed_by_permissions_boundary"] = (
            child_allowed_by_permissions_boundary.text or ""
        ).lower() == "true"
    else:
        out["allowed_by_permissions_boundary"] = False
    return out
