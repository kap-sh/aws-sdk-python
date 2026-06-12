"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalReplicationGroupMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.global_replication_group_member

GlobalReplicationGroupMemberList: TypeAlias = list[
    "aws_sdk_elasticache.types.global_replication_group_member.GlobalReplicationGroupMember"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalReplicationGroupMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.global_replication_group_member

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.global_replication_group_member.serialize_query(
            item, pairs, f"{prefix}.GlobalReplicationGroupMember.{n}"
        )


def deserialize_query(el: Element) -> GlobalReplicationGroupMemberList:
    import aws_sdk_elasticache.types.global_replication_group_member

    out: GlobalReplicationGroupMemberList = []
    for child in el.findall("GlobalReplicationGroupMember"):
        out.append(
            aws_sdk_elasticache.types.global_replication_group_member.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: GlobalReplicationGroupMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.global_replication_group_member

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.global_replication_group_member.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> GlobalReplicationGroupMemberList:
    import aws_sdk_elasticache.types.global_replication_group_member

    out: GlobalReplicationGroupMemberList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.global_replication_group_member.deserialize_query(
                child
            )
        )
    return out
