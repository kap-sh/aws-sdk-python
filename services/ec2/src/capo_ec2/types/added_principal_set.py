"""Generated from Smithy shape ``com.amazonaws.ec2#AddedPrincipalSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.added_principal

AddedPrincipalSet: TypeAlias = list["capo_ec2.types.added_principal.AddedPrincipal"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AddedPrincipalSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.added_principal

        capo_ec2.types.added_principal.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> AddedPrincipalSet:
    import capo_ec2.types.added_principal

    out: AddedPrincipalSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.added_principal.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> AddedPrincipalSet:
    import capo_ec2.types.added_principal

    out: AddedPrincipalSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.added_principal.deserialize_ec2_query(child))
    return out
