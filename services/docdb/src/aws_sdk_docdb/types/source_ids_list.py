"""Generated from Smithy shape ``com.amazonaws.docdb#SourceIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.string

SourceIdsList: TypeAlias = list["aws_sdk_docdb.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.SourceId.{n}", str(item)))


def deserialize_query(el: Element) -> SourceIdsList:
    out: SourceIdsList = []
    for child in el.findall("SourceId"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: SourceIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SourceIdsList:
    out: SourceIdsList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
