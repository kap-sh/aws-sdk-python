"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeGroupMemberUpdateStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.node_update_initiated_by
    import capo_elasticache.types.node_update_status
    import capo_elasticache.types.string
    import capo_elasticache.types.t_stamp


class NodeGroupMemberUpdateStatus(TypedDict, closed=True):
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cache cluster ID</p>"""
    cache_node_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The node ID of the cache cluster</p>"""
    node_update_status: NotRequired[
        "capo_elasticache.types.node_update_status.NodeUpdateStatus"
    ]
    """<p>The update status of the node</p>"""
    node_deletion_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The deletion date of the node</p>"""
    node_update_start_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The start date of the update for a node</p>"""
    node_update_end_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The end date of the update for a node</p>"""
    node_update_initiated_by: NotRequired[
        "capo_elasticache.types.node_update_initiated_by.NodeUpdateInitiatedBy"
    ]
    """<p>Reflects whether the update was initiated by the customer or automatically applied</p>"""
    node_update_initiated_date: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date when the update is triggered</p>"""
    node_update_status_modified_date: NotRequired[
        "capo_elasticache.types.t_stamp.TStamp"
    ]
    """<p>The date when the NodeUpdateStatus was last modified</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeGroupMemberUpdateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "cache_node_id" in value:
        pairs.append((f"{prefix}.CacheNodeId", str(value["cache_node_id"])))
    if "node_update_status" in value:
        import capo_elasticache.types.node_update_status

        capo_elasticache.types.node_update_status.serialize_query(
            value["node_update_status"], pairs, f"{prefix}.NodeUpdateStatus"
        )
    if "node_deletion_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["node_deletion_date"], pairs, f"{prefix}.NodeDeletionDate"
        )
    if "node_update_start_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["node_update_start_date"], pairs, f"{prefix}.NodeUpdateStartDate"
        )
    if "node_update_end_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["node_update_end_date"], pairs, f"{prefix}.NodeUpdateEndDate"
        )
    if "node_update_initiated_by" in value:
        import capo_elasticache.types.node_update_initiated_by

        capo_elasticache.types.node_update_initiated_by.serialize_query(
            value["node_update_initiated_by"], pairs, f"{prefix}.NodeUpdateInitiatedBy"
        )
    if "node_update_initiated_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["node_update_initiated_date"],
            pairs,
            f"{prefix}.NodeUpdateInitiatedDate",
        )
    if "node_update_status_modified_date" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["node_update_status_modified_date"],
            pairs,
            f"{prefix}.NodeUpdateStatusModifiedDate",
        )


def deserialize_query(el: Element) -> NodeGroupMemberUpdateStatus:
    out: NodeGroupMemberUpdateStatus = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_cache_node_id = el.find("CacheNodeId")
    if child_cache_node_id is not None:
        out["cache_node_id"] = str(child_cache_node_id.text or "")
    child_node_update_status = el.find("NodeUpdateStatus")
    if child_node_update_status is not None:
        import capo_elasticache.types.node_update_status

        out["node_update_status"] = (
            capo_elasticache.types.node_update_status.deserialize_query(
                child_node_update_status
            )
        )
    child_node_deletion_date = el.find("NodeDeletionDate")
    if child_node_deletion_date is not None:
        import capo_elasticache.types.t_stamp

        out["node_deletion_date"] = capo_elasticache.types.t_stamp.deserialize_query(
            child_node_deletion_date
        )
    child_node_update_start_date = el.find("NodeUpdateStartDate")
    if child_node_update_start_date is not None:
        import capo_elasticache.types.t_stamp

        out["node_update_start_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_node_update_start_date
            )
        )
    child_node_update_end_date = el.find("NodeUpdateEndDate")
    if child_node_update_end_date is not None:
        import capo_elasticache.types.t_stamp

        out["node_update_end_date"] = capo_elasticache.types.t_stamp.deserialize_query(
            child_node_update_end_date
        )
    child_node_update_initiated_by = el.find("NodeUpdateInitiatedBy")
    if child_node_update_initiated_by is not None:
        import capo_elasticache.types.node_update_initiated_by

        out["node_update_initiated_by"] = (
            capo_elasticache.types.node_update_initiated_by.deserialize_query(
                child_node_update_initiated_by
            )
        )
    child_node_update_initiated_date = el.find("NodeUpdateInitiatedDate")
    if child_node_update_initiated_date is not None:
        import capo_elasticache.types.t_stamp

        out["node_update_initiated_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_node_update_initiated_date
            )
        )
    child_node_update_status_modified_date = el.find("NodeUpdateStatusModifiedDate")
    if child_node_update_status_modified_date is not None:
        import capo_elasticache.types.t_stamp

        out["node_update_status_modified_date"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_node_update_status_modified_date
            )
        )
    return out
