"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.node_group

NodeGroupList: TypeAlias = list["capo_elasticache.types.node_group.NodeGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_group

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_group.serialize_query(
            item, pairs, f"{prefix}.NodeGroup.{n}"
        )


def deserialize_query(el: Element) -> NodeGroupList:
    import capo_elasticache.types.node_group

    out: NodeGroupList = []
    for child in el.findall("NodeGroup"):
        out.append(capo_elasticache.types.node_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: NodeGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_group

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> NodeGroupList:
    import capo_elasticache.types.node_group

    out: NodeGroupList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.node_group.deserialize_query(child))
    return out
