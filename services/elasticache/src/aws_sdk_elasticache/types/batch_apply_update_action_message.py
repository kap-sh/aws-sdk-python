"""Generated from Smithy shape ``com.amazonaws.elasticache#BatchApplyUpdateActionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_cluster_id_list
    import aws_sdk_elasticache.types.replication_group_id_list
    import aws_sdk_elasticache.types.string


class BatchApplyUpdateActionMessage(TypedDict, closed=True):
    replication_group_ids: NotRequired[
        "aws_sdk_elasticache.types.replication_group_id_list.ReplicationGroupIdList"
    ]
    """<p>The replication group IDs</p>"""
    cache_cluster_ids: NotRequired[
        "aws_sdk_elasticache.types.cache_cluster_id_list.CacheClusterIdList"
    ]
    """<p>The cache cluster IDs</p>"""
    service_update_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The unique ID of the service update</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchApplyUpdateActionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_ids" in value:
        import aws_sdk_elasticache.types.replication_group_id_list

        aws_sdk_elasticache.types.replication_group_id_list.serialize_query(
            value["replication_group_ids"], pairs, f"{prefix}.ReplicationGroupIds"
        )
    if "cache_cluster_ids" in value:
        import aws_sdk_elasticache.types.cache_cluster_id_list

        aws_sdk_elasticache.types.cache_cluster_id_list.serialize_query(
            value["cache_cluster_ids"], pairs, f"{prefix}.CacheClusterIds"
        )
    if "service_update_name" in value:
        pairs.append((f"{prefix}.ServiceUpdateName", str(value["service_update_name"])))


def deserialize_query(el: Element) -> BatchApplyUpdateActionMessage:
    out: BatchApplyUpdateActionMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_ids = el.find("ReplicationGroupIds")
    if child_replication_group_ids is not None:
        import aws_sdk_elasticache.types.replication_group_id_list

        out["replication_group_ids"] = (
            aws_sdk_elasticache.types.replication_group_id_list.deserialize_query(
                child_replication_group_ids
            )
        )
    child_cache_cluster_ids = el.find("CacheClusterIds")
    if child_cache_cluster_ids is not None:
        import aws_sdk_elasticache.types.cache_cluster_id_list

        out["cache_cluster_ids"] = (
            aws_sdk_elasticache.types.cache_cluster_id_list.deserialize_query(
                child_cache_cluster_ids
            )
        )
    child_service_update_name = el.find("ServiceUpdateName")
    if child_service_update_name is not None:
        out["service_update_name"] = str(child_service_update_name.text or "")
    return out
