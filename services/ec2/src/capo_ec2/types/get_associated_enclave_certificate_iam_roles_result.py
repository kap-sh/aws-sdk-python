"""Generated from Smithy shape ``com.amazonaws.ec2#GetAssociatedEnclaveCertificateIamRolesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.associated_roles_list


class GetAssociatedEnclaveCertificateIamRolesResult(TypedDict, closed=True):
    associated_roles: NotRequired[
        "capo_ec2.types.associated_roles_list.AssociatedRolesList"
    ]
    """<p>Information about the associated IAM roles.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAssociatedEnclaveCertificateIamRolesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "associated_roles" in value:
        import capo_ec2.types.associated_roles_list

        capo_ec2.types.associated_roles_list.serialize_ec2_query(
            value["associated_roles"], pairs, f"{key_prefix}AssociatedRoleSet"
        )


def deserialize_ec2_query(el: Element) -> GetAssociatedEnclaveCertificateIamRolesResult:
    out: GetAssociatedEnclaveCertificateIamRolesResult = {}  # type: ignore[typeddict-item]
    if el.find("associatedRoleSet") is not None:
        import capo_ec2.types.associated_roles_list

        out["associated_roles"] = (
            capo_ec2.types.associated_roles_list.deserialize_ec2_query(
                el, "associatedRoleSet"
            )
        )
    return out
