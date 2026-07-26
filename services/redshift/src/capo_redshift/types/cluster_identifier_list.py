"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string

ClusterIdentifierList: TypeAlias = list["capo_redshift.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterIdentifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.ClusterIdentifier.{n}", str(item)))


def deserialize_query(el: Element) -> ClusterIdentifierList:
    out: ClusterIdentifierList = []
    for child in el.findall("ClusterIdentifier"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ClusterIdentifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ClusterIdentifierList:
    out: ClusterIdentifierList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
