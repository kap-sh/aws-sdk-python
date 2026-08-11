"""Generated from Smithy shape ``com.amazonaws.rds#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter

FilterList: TypeAlias = list["capo_rds.types.filter.Filter"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.filter

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.filter.serialize_query(item, pairs, f"{prefix}.Filter.{n}")


def deserialize_query(el: Element) -> FilterList:
    import capo_rds.types.filter

    out: FilterList = []
    for child in el.findall("Filter"):
        out.append(capo_rds.types.filter.deserialize_query(child))
    return out


def serialize_query_flat(
    value: FilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.filter

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.filter.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> FilterList:
    import capo_rds.types.filter

    out: FilterList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.filter.deserialize_query(child))
    return out
