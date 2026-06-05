"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedRolesList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_role

AssociatedRolesList: TypeAlias = list[
    "aws_sdk_ec2.types.associated_role.AssociatedRole"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociatedRolesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.associated_role

        aws_sdk_ec2.types.associated_role.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AssociatedRolesList:
    import aws_sdk_ec2.types.associated_role

    out: AssociatedRolesList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.associated_role.deserialize_ec2_query(child))
    return out
