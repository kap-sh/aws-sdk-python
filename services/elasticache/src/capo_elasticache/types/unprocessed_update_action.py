"""Generated from Smithy shape ``com.amazonaws.elasticache#UnprocessedUpdateAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class UnprocessedUpdateAction(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The replication group ID</p>"""
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The ID of the cache cluster</p>"""
    service_update_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    error_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The error type for requests that are not processed</p>"""
    error_message: NotRequired["capo_elasticache.types.string.String"]
    """<p>The error message that describes the reason the request was not processed</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UnprocessedUpdateAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "service_update_name" in value:
        pairs.append((f"{prefix}.ServiceUpdateName", str(value["service_update_name"])))
    if "error_type" in value:
        pairs.append((f"{prefix}.ErrorType", str(value["error_type"])))
    if "error_message" in value:
        pairs.append((f"{prefix}.ErrorMessage", str(value["error_message"])))


def deserialize_query(el: Element) -> UnprocessedUpdateAction:
    out: UnprocessedUpdateAction = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_service_update_name = el.find("ServiceUpdateName")
    if child_service_update_name is not None:
        out["service_update_name"] = str(child_service_update_name.text or "")
    child_error_type = el.find("ErrorType")
    if child_error_type is not None:
        out["error_type"] = str(child_error_type.text or "")
    child_error_message = el.find("ErrorMessage")
    if child_error_message is not None:
        out["error_message"] = str(child_error_message.text or "")
    return out
