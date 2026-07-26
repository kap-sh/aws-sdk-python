"""Generated from Smithy shape ``com.amazonaws.docdb#SubnetList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.subnet

SubnetList: TypeAlias = list["capo_docdb.types.subnet.Subnet"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_docdb.types.subnet

    for n, item in enumerate(value, 1):
        capo_docdb.types.subnet.serialize_query(item, pairs, f"{prefix}.Subnet.{n}")


def deserialize_query(el: Element) -> SubnetList:
    import capo_docdb.types.subnet

    out: SubnetList = []
    for child in el.findall("Subnet"):
        out.append(capo_docdb.types.subnet.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SubnetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_docdb.types.subnet

    for n, item in enumerate(value, 1):
        capo_docdb.types.subnet.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SubnetList:
    import capo_docdb.types.subnet

    out: SubnetList = []
    for child in parent.findall(tag):
        out.append(capo_docdb.types.subnet.deserialize_query(child))
    return out
