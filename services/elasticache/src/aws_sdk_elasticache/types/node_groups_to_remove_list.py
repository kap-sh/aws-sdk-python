"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupsToRemoveList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.allowed_node_group_id

NodeGroupsToRemoveList: TypeAlias = list[
    "aws_sdk_elasticache.types.allowed_node_group_id.AllowedNodeGroupId"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupsToRemoveList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.NodeGroupToRemove.{n}", str(item)))


def deserialize_query(el: Element) -> NodeGroupsToRemoveList:
    out: NodeGroupsToRemoveList = []
    for child in el.findall("NodeGroupToRemove"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: NodeGroupsToRemoveList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> NodeGroupsToRemoveList:
    out: NodeGroupsToRemoveList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
