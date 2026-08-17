"""Generated from Smithy shape ``com.amazonaws.ec2#IpamScopeSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_scope

IpamScopeSet: TypeAlias = list["capo_ec2.types.ipam_scope.IpamScope"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamScopeSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_scope

        capo_ec2.types.ipam_scope.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> IpamScopeSet:
    import capo_ec2.types.ipam_scope

    out: IpamScopeSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ipam_scope.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> IpamScopeSet:
    import capo_ec2.types.ipam_scope

    out: IpamScopeSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_scope.deserialize_ec2_query(child))
    return out
