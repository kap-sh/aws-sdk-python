"""Generated from Smithy shape ``com.amazonaws.elasticache#ProcessedUpdateAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string
    import capo_elasticache.types.update_action_status


class ProcessedUpdateAction(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the replication group</p>"""
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the cache cluster</p>"""
    service_update_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    update_action_status: NotRequired[
        "capo_elasticache.types.update_action_status.UpdateActionStatus"
    ]
    """<p>The status of the update action on the Valkey or Redis OSS cluster</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ProcessedUpdateAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "service_update_name" in value:
        pairs.append((f"{prefix}.ServiceUpdateName", str(value["service_update_name"])))
    if "update_action_status" in value:
        import capo_elasticache.types.update_action_status

        capo_elasticache.types.update_action_status.serialize_query(
            value["update_action_status"], pairs, f"{prefix}.UpdateActionStatus"
        )


def deserialize_query(el: Element) -> ProcessedUpdateAction:
    out: ProcessedUpdateAction = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_service_update_name = el.find("ServiceUpdateName")
    if child_service_update_name is not None:
        out["service_update_name"] = str(child_service_update_name.text or "")
    child_update_action_status = el.find("UpdateActionStatus")
    if child_update_action_status is not None:
        import capo_elasticache.types.update_action_status

        out["update_action_status"] = (
            capo_elasticache.types.update_action_status.deserialize_query(
                child_update_action_status
            )
        )
    return out
