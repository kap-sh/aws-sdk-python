"""Generated from Smithy shape ``com.amazonaws.elasticache#ReplicationGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.replication_group

ReplicationGroupList: TypeAlias = list[
    "capo_elasticache.types.replication_group.ReplicationGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReplicationGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.replication_group

    for n, item in enumerate(value, 1):
        capo_elasticache.types.replication_group.serialize_query(
            item, pairs, f"{prefix}.ReplicationGroup.{n}"
        )


def deserialize_query(el: Element) -> ReplicationGroupList:
    import capo_elasticache.types.replication_group

    out: ReplicationGroupList = []
    for child in el.findall("ReplicationGroup"):
        out.append(capo_elasticache.types.replication_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReplicationGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.replication_group

    for n, item in enumerate(value, 1):
        capo_elasticache.types.replication_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReplicationGroupList:
    import capo_elasticache.types.replication_group

    out: ReplicationGroupList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.replication_group.deserialize_query(child))
    return out
