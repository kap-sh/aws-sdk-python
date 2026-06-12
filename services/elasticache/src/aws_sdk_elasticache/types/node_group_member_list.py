"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupMemberList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.node_group_member

NodeGroupMemberList: TypeAlias = list[
    "aws_sdk_elasticache.types.node_group_member.NodeGroupMember"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.node_group_member

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.node_group_member.serialize_query(
            item, pairs, f"{prefix}.NodeGroupMember.{n}"
        )


def deserialize_query(el: Element) -> NodeGroupMemberList:
    import aws_sdk_elasticache.types.node_group_member

    out: NodeGroupMemberList = []
    for child in el.findall("NodeGroupMember"):
        out.append(aws_sdk_elasticache.types.node_group_member.deserialize_query(child))
    return out


def serialize_query_flat(
    value: NodeGroupMemberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.node_group_member

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.node_group_member.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NodeGroupMemberList:
    import aws_sdk_elasticache.types.node_group_member

    out: NodeGroupMemberList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.node_group_member.deserialize_query(child))
    return out
