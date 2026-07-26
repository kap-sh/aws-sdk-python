"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.node_group_configuration

NodeGroupConfigurationList: TypeAlias = list[
    "capo_elasticache.types.node_group_configuration.NodeGroupConfiguration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_group_configuration

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_group_configuration.serialize_query(
            item, pairs, f"{prefix}.NodeGroupConfiguration.{n}"
        )


def deserialize_query(el: Element) -> NodeGroupConfigurationList:
    import capo_elasticache.types.node_group_configuration

    out: NodeGroupConfigurationList = []
    for child in el.findall("NodeGroupConfiguration"):
        out.append(
            capo_elasticache.types.node_group_configuration.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: NodeGroupConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_group_configuration

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_group_configuration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NodeGroupConfigurationList:
    import capo_elasticache.types.node_group_configuration

    out: NodeGroupConfigurationList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.node_group_configuration.deserialize_query(child)
        )
    return out
