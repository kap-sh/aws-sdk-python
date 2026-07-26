"""Generated from Smithy shape ``com.amazonaws.elasticache#DecreaseNodeGroupsInGlobalReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean
    import capo_elasticache.types.global_node_group_id_list
    import capo_elasticache.types.integer
    import capo_elasticache.types.string


class DecreaseNodeGroupsInGlobalReplicationGroupMessage(TypedDict, closed=True):
    global_replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    node_group_count: NotRequired["capo_elasticache.types.integer.Integer"]
    """<p>The number of node groups (shards) that results from the modification of the shard configuration</p>"""
    global_node_groups_to_remove: NotRequired[
        "capo_elasticache.types.global_node_group_id_list.GlobalNodeGroupIdList"
    ]
    """<p>If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. GlobalNodeGroupsToRemove is a list of NodeGroupIds to remove from the cluster. ElastiCache will attempt to remove all node groups listed by GlobalNodeGroupsToRemove from the cluster. </p>"""
    global_node_groups_to_retain: NotRequired[
        "capo_elasticache.types.global_node_group_id_list.GlobalNodeGroupIdList"
    ]
    """<p>If the value of NodeGroupCount is less than the current number of node groups (shards), then either NodeGroupsToRemove or NodeGroupsToRetain is required. GlobalNodeGroupsToRetain is a list of NodeGroupIds to retain from the cluster. ElastiCache will attempt to retain all node groups listed by GlobalNodeGroupsToRetain from the cluster. </p>"""
    apply_immediately: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p>Indicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is true. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DecreaseNodeGroupsInGlobalReplicationGroupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "global_replication_group_id" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupId",
                str(value["global_replication_group_id"]),
            )
        )
    if "node_group_count" in value:
        pairs.append((f"{prefix}.NodeGroupCount", str(value["node_group_count"])))
    if "global_node_groups_to_remove" in value:
        import capo_elasticache.types.global_node_group_id_list

        capo_elasticache.types.global_node_group_id_list.serialize_query(
            value["global_node_groups_to_remove"],
            pairs,
            f"{prefix}.GlobalNodeGroupsToRemove",
        )
    if "global_node_groups_to_retain" in value:
        import capo_elasticache.types.global_node_group_id_list

        capo_elasticache.types.global_node_group_id_list.serialize_query(
            value["global_node_groups_to_retain"],
            pairs,
            f"{prefix}.GlobalNodeGroupsToRetain",
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )


def deserialize_query(el: Element) -> DecreaseNodeGroupsInGlobalReplicationGroupMessage:
    out: DecreaseNodeGroupsInGlobalReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_node_group_count = el.find("NodeGroupCount")
    if child_node_group_count is not None:
        out["node_group_count"] = int(child_node_group_count.text or "")
    child_global_node_groups_to_remove = el.find("GlobalNodeGroupsToRemove")
    if child_global_node_groups_to_remove is not None:
        import capo_elasticache.types.global_node_group_id_list

        out["global_node_groups_to_remove"] = (
            capo_elasticache.types.global_node_group_id_list.deserialize_query(
                child_global_node_groups_to_remove
            )
        )
    child_global_node_groups_to_retain = el.find("GlobalNodeGroupsToRetain")
    if child_global_node_groups_to_retain is not None:
        import capo_elasticache.types.global_node_group_id_list

        out["global_node_groups_to_retain"] = (
            capo_elasticache.types.global_node_group_id_list.deserialize_query(
                child_global_node_groups_to_retain
            )
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    return out
