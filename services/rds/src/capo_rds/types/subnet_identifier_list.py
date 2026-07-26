"""Generated from Smithy shape ``com.amazonaws.rds#SubnetIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string

SubnetIdentifierList: TypeAlias = list["capo_rds.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetIdentifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.SubnetIdentifier.{n}", str(item)))


def deserialize_query(el: Element) -> SubnetIdentifierList:
    out: SubnetIdentifierList = []
    for child in el.findall("SubnetIdentifier"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: SubnetIdentifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SubnetIdentifierList:
    out: SubnetIdentifierList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
