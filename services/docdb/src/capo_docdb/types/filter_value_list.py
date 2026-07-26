"""Generated from Smithy shape ``com.amazonaws.docdb#FilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string

FilterValueList: TypeAlias = list["capo_docdb.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: FilterValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.Value.{n}", str(item)))


def deserialize_query(el: Element) -> FilterValueList:
    out: FilterValueList = []
    for child in el.findall("Value"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: FilterValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> FilterValueList:
    out: FilterValueList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
