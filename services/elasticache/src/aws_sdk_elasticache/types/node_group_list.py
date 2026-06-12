"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.node_group

NodeGroupList: TypeAlias = list["aws_sdk_elasticache.types.node_group.NodeGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.node_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.node_group.serialize_query(
            item, pairs, f"{prefix}.NodeGroup.{n}"
        )


def deserialize_query(el: Element) -> NodeGroupList:
    import aws_sdk_elasticache.types.node_group

    out: NodeGroupList = []
    for child in el.findall("NodeGroup"):
        out.append(aws_sdk_elasticache.types.node_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: NodeGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.node_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.node_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NodeGroupList:
    import aws_sdk_elasticache.types.node_group

    out: NodeGroupList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.node_group.deserialize_query(child))
    return out
