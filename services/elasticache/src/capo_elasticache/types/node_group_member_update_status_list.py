"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupMemberUpdateStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.node_group_member_update_status

NodeGroupMemberUpdateStatusList: TypeAlias = list[
    "capo_elasticache.types.node_group_member_update_status.NodeGroupMemberUpdateStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupMemberUpdateStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_group_member_update_status

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_group_member_update_status.serialize_query(
            item, pairs, f"{prefix}.NodeGroupMemberUpdateStatus.{n}"
        )


def deserialize_query(el: Element) -> NodeGroupMemberUpdateStatusList:
    import capo_elasticache.types.node_group_member_update_status

    out: NodeGroupMemberUpdateStatusList = []
    for child in el.findall("NodeGroupMemberUpdateStatus"):
        out.append(
            capo_elasticache.types.node_group_member_update_status.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: NodeGroupMemberUpdateStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_group_member_update_status

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_group_member_update_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> NodeGroupMemberUpdateStatusList:
    import capo_elasticache.types.node_group_member_update_status

    out: NodeGroupMemberUpdateStatusList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.node_group_member_update_status.deserialize_query(
                child
            )
        )
    return out
