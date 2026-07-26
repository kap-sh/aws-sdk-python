"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupUpdateStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.node_group_update_status

NodeGroupUpdateStatusList: TypeAlias = list[
    "capo_elasticache.types.node_group_update_status.NodeGroupUpdateStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupUpdateStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_group_update_status

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_group_update_status.serialize_query(
            item, pairs, f"{prefix}.NodeGroupUpdateStatus.{n}"
        )


def deserialize_query(el: Element) -> NodeGroupUpdateStatusList:
    import capo_elasticache.types.node_group_update_status

    out: NodeGroupUpdateStatusList = []
    for child in el.findall("NodeGroupUpdateStatus"):
        out.append(
            capo_elasticache.types.node_group_update_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: NodeGroupUpdateStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_group_update_status

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_group_update_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NodeGroupUpdateStatusList:
    import capo_elasticache.types.node_group_update_status

    out: NodeGroupUpdateStatusList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.node_group_update_status.deserialize_query(child)
        )
    return out
