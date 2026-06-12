"""Generated from Smithy shape ``com.amazonaws.docdb#ReadReplicaIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.string

ReadReplicaIdentifierList: TypeAlias = list["aws_sdk_docdb.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReadReplicaIdentifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.ReadReplicaIdentifier.{n}", str(item)))


def deserialize_query(el: Element) -> ReadReplicaIdentifierList:
    out: ReadReplicaIdentifierList = []
    for child in el.findall("ReadReplicaIdentifier"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ReadReplicaIdentifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ReadReplicaIdentifierList:
    out: ReadReplicaIdentifierList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
