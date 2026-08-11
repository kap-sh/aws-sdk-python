"""Generated from Smithy shape ``com.amazonaws.ec2#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.filter

FilterList: TypeAlias = list["capo_ec2.types.filter.Filter"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.filter

        capo_ec2.types.filter.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> FilterList:
    import capo_ec2.types.filter

    out: FilterList = []
    for child in el.findall("Filter"):
        out.append(capo_ec2.types.filter.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> FilterList:
    import capo_ec2.types.filter

    out: FilterList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.filter.deserialize_ec2_query(child))
    return out
