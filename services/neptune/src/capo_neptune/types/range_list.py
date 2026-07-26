"""Generated from Smithy shape ``com.amazonaws.neptune#RangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.range

RangeList: TypeAlias = list["capo_neptune.types.range.Range"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.range

    for n, item in enumerate(value, 1):
        capo_neptune.types.range.serialize_query(item, pairs, f"{prefix}.Range.{n}")


def deserialize_query(el: Element) -> RangeList:
    import capo_neptune.types.range

    out: RangeList = []
    for child in el.findall("Range"):
        out.append(capo_neptune.types.range.deserialize_query(child))
    return out


def serialize_query_flat(
    value: RangeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.range

    for n, item in enumerate(value, 1):
        capo_neptune.types.range.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> RangeList:
    import capo_neptune.types.range

    out: RangeList = []
    for child in parent.findall(tag):
        out.append(capo_neptune.types.range.deserialize_query(child))
    return out
