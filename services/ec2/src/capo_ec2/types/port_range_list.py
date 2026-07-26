"""Generated from Smithy shape ``com.amazonaws.ec2#PortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.port_range

PortRangeList: TypeAlias = list["capo_ec2.types.port_range.PortRange"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PortRangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.port_range

        capo_ec2.types.port_range.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> PortRangeList:
    import capo_ec2.types.port_range

    out: PortRangeList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.port_range.deserialize_ec2_query(child))
    return out
