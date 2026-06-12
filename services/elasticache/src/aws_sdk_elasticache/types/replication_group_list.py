"""Generated from Smithy shape ``com.amazonaws.elasticache#ReplicationGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.replication_group

ReplicationGroupList: TypeAlias = list[
    "aws_sdk_elasticache.types.replication_group.ReplicationGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReplicationGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.replication_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.replication_group.serialize_query(
            item, pairs, f"{prefix}.ReplicationGroup.{n}"
        )


def deserialize_query(el: Element) -> ReplicationGroupList:
    import aws_sdk_elasticache.types.replication_group

    out: ReplicationGroupList = []
    for child in el.findall("ReplicationGroup"):
        out.append(aws_sdk_elasticache.types.replication_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReplicationGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.replication_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.replication_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReplicationGroupList:
    import aws_sdk_elasticache.types.replication_group

    out: ReplicationGroupList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.replication_group.deserialize_query(child))
    return out
