"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string

NodeTypeList: TypeAlias = list["capo_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> NodeTypeList:
    out: NodeTypeList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: NodeTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> NodeTypeList:
    out: NodeTypeList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
