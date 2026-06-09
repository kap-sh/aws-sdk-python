"""Generated from Smithy shape ``com.amazonaws.ec2#GetAssociatedEnclaveCertificateIamRolesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_roles_list


class GetAssociatedEnclaveCertificateIamRolesResult(TypedDict):
    associated_roles: NotRequired[
        "aws_sdk_ec2.types.associated_roles_list.AssociatedRolesList"
    ]
    """<p>Information about the associated IAM roles.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAssociatedEnclaveCertificateIamRolesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "associated_roles" in value:
        import aws_sdk_ec2.types.associated_roles_list

        aws_sdk_ec2.types.associated_roles_list.serialize_ec2_query(
            value["associated_roles"], pairs, f"{prefix}.AssociatedRoleSet"
        )


def deserialize_ec2_query(el: Element) -> GetAssociatedEnclaveCertificateIamRolesResult:
    out: GetAssociatedEnclaveCertificateIamRolesResult = {}  # type: ignore[typeddict-item]
    if el.find("AssociatedRoleSet") is not None:
        import aws_sdk_ec2.types.associated_roles_list

        out["associated_roles"] = (
            aws_sdk_ec2.types.associated_roles_list.deserialize_ec2_query(
                el, "AssociatedRoleSet"
            )
        )
    return out
