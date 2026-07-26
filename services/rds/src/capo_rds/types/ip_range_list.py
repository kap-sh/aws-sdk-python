"""Generated from Smithy shape ``com.amazonaws.rds#IPRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.ip_range

IPRangeList: TypeAlias = list["capo_rds.types.ip_range.IPRange"]


# --- awsQuery ser/de ---
def serialize_query(
    value: IPRangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.ip_range

    for n, item in enumerate(value, 1):
        capo_rds.types.ip_range.serialize_query(item, pairs, f"{prefix}.IPRange.{n}")


def deserialize_query(el: Element) -> IPRangeList:
    import capo_rds.types.ip_range

    out: IPRangeList = []
    for child in el.findall("IPRange"):
        out.append(capo_rds.types.ip_range.deserialize_query(child))
    return out


def serialize_query_flat(
    value: IPRangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.ip_range

    for n, item in enumerate(value, 1):
        capo_rds.types.ip_range.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> IPRangeList:
    import capo_rds.types.ip_range

    out: IPRangeList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.ip_range.deserialize_query(child))
    return out
