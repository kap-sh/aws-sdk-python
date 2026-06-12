"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheNodeIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string

CacheNodeIdsList: TypeAlias = list["aws_sdk_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheNodeIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.CacheNodeId.{n}", str(item)))


def deserialize_query(el: Element) -> CacheNodeIdsList:
    out: CacheNodeIdsList = []
    for child in el.findall("CacheNodeId"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: CacheNodeIdsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> CacheNodeIdsList:
    out: CacheNodeIdsList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
