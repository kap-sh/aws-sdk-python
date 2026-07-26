"""Generated from Smithy shape ``com.amazonaws.elasticache#ReplicationGroupOutpostArnList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string

ReplicationGroupOutpostArnList: TypeAlias = list["capo_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReplicationGroupOutpostArnList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.ReplicationGroupOutpostArn.{n}", str(item)))


def deserialize_query(el: Element) -> ReplicationGroupOutpostArnList:
    out: ReplicationGroupOutpostArnList = []
    for child in el.findall("ReplicationGroupOutpostArn"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ReplicationGroupOutpostArnList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ReplicationGroupOutpostArnList:
    out: ReplicationGroupOutpostArnList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
