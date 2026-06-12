"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalReplicationGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.global_replication_group

GlobalReplicationGroupList: TypeAlias = list[
    "aws_sdk_elasticache.types.global_replication_group.GlobalReplicationGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalReplicationGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.global_replication_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.global_replication_group.serialize_query(
            item, pairs, f"{prefix}.GlobalReplicationGroup.{n}"
        )


def deserialize_query(el: Element) -> GlobalReplicationGroupList:
    import aws_sdk_elasticache.types.global_replication_group

    out: GlobalReplicationGroupList = []
    for child in el.findall("GlobalReplicationGroup"):
        out.append(
            aws_sdk_elasticache.types.global_replication_group.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: GlobalReplicationGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.global_replication_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.global_replication_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> GlobalReplicationGroupList:
    import aws_sdk_elasticache.types.global_replication_group

    out: GlobalReplicationGroupList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.global_replication_group.deserialize_query(child)
        )
    return out
