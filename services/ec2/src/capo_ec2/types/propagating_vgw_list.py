"""Generated from Smithy shape ``com.amazonaws.ec2#PropagatingVgwList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.propagating_vgw

PropagatingVgwList: TypeAlias = list["capo_ec2.types.propagating_vgw.PropagatingVgw"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PropagatingVgwList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.propagating_vgw

        capo_ec2.types.propagating_vgw.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> PropagatingVgwList:
    import capo_ec2.types.propagating_vgw

    out: PropagatingVgwList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.propagating_vgw.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PropagatingVgwList:
    import capo_ec2.types.propagating_vgw

    out: PropagatingVgwList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.propagating_vgw.deserialize_ec2_query(child))
    return out
