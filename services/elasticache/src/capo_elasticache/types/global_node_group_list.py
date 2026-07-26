"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalNodeGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.global_node_group

GlobalNodeGroupList: TypeAlias = list[
    "capo_elasticache.types.global_node_group.GlobalNodeGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalNodeGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.global_node_group

    for n, item in enumerate(value, 1):
        capo_elasticache.types.global_node_group.serialize_query(
            item, pairs, f"{prefix}.GlobalNodeGroup.{n}"
        )


def deserialize_query(el: Element) -> GlobalNodeGroupList:
    import capo_elasticache.types.global_node_group

    out: GlobalNodeGroupList = []
    for child in el.findall("GlobalNodeGroup"):
        out.append(capo_elasticache.types.global_node_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: GlobalNodeGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.global_node_group

    for n, item in enumerate(value, 1):
        capo_elasticache.types.global_node_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> GlobalNodeGroupList:
    import capo_elasticache.types.global_node_group

    out: GlobalNodeGroupList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.global_node_group.deserialize_query(child))
    return out
