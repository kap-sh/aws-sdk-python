"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedRolesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.associated_role

AssociatedRolesList: TypeAlias = list["capo_ec2.types.associated_role.AssociatedRole"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociatedRolesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.associated_role

        capo_ec2.types.associated_role.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> AssociatedRolesList:
    import capo_ec2.types.associated_role

    out: AssociatedRolesList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.associated_role.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AssociatedRolesList:
    import capo_ec2.types.associated_role

    out: AssociatedRolesList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.associated_role.deserialize_ec2_query(child))
    return out
