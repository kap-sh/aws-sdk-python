"""Generated from Smithy shape ``com.amazonaws.ec2#IpRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ip_range

IpRangeList: TypeAlias = list["capo_ec2.types.ip_range.IpRange"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpRangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ip_range

        capo_ec2.types.ip_range.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> IpRangeList:
    import capo_ec2.types.ip_range

    out: IpRangeList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ip_range.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> IpRangeList:
    import capo_ec2.types.ip_range

    out: IpRangeList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ip_range.deserialize_ec2_query(child))
    return out
