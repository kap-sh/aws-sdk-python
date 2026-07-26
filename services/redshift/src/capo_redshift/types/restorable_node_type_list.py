"""Generated from Smithy shape ``com.amazonaws.redshift#RestorableNodeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string

RestorableNodeTypeList: TypeAlias = list["capo_redshift.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: RestorableNodeTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.NodeType.{n}", str(item)))


def deserialize_query(el: Element) -> RestorableNodeTypeList:
    out: RestorableNodeTypeList = []
    for child in el.findall("NodeType"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: RestorableNodeTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> RestorableNodeTypeList:
    out: RestorableNodeTypeList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
