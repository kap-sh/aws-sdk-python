"""Generated from Smithy shape ``com.amazonaws.rds#RangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.range

RangeList: TypeAlias = list["capo_rds.types.range.Range"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.range

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.range.serialize_query(item, pairs, f"{prefix}.Range.{n}")


def deserialize_query(el: Element) -> RangeList:
    import capo_rds.types.range

    out: RangeList = []
    for child in el.findall("Range"):
        out.append(capo_rds.types.range.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.range

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.range.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> RangeList:
    import capo_rds.types.range

    out: RangeList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.range.deserialize_query(child))
    return out
