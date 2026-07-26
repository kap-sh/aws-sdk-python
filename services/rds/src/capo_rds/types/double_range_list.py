"""Generated from Smithy shape ``com.amazonaws.rds#DoubleRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.double_range

DoubleRangeList: TypeAlias = list["capo_rds.types.double_range.DoubleRange"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DoubleRangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.double_range

    for n, item in enumerate(value, 1):
        capo_rds.types.double_range.serialize_query(
            item, pairs, f"{prefix}.DoubleRange.{n}"
        )


def deserialize_query(el: Element) -> DoubleRangeList:
    import capo_rds.types.double_range

    out: DoubleRangeList = []
    for child in el.findall("DoubleRange"):
        out.append(capo_rds.types.double_range.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DoubleRangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.double_range

    for n, item in enumerate(value, 1):
        capo_rds.types.double_range.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DoubleRangeList:
    import capo_rds.types.double_range

    out: DoubleRangeList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.double_range.deserialize_query(child))
    return out
