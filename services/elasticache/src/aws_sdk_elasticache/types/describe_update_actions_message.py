"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeUpdateActionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean_optional
    import aws_sdk_elasticache.types.cache_cluster_id_list
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.replication_group_id_list
    import aws_sdk_elasticache.types.service_update_status_list
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.time_range_filter
    import aws_sdk_elasticache.types.update_action_status_list


class DescribeUpdateActionsMessage(TypedDict, closed=True):
    service_update_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    replication_group_ids: NotRequired[
        "aws_sdk_elasticache.types.replication_group_id_list.ReplicationGroupIdList"
    ]
    """<p>The replication group IDs</p>"""
    cache_cluster_ids: NotRequired[
        "aws_sdk_elasticache.types.cache_cluster_id_list.CacheClusterIdList"
    ]
    """<p>The cache cluster IDs</p>"""
    engine: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Elasticache engine to which the update applies. Either Valkey, Redis OSS or Memcached.</p>"""
    service_update_status: NotRequired[
        "aws_sdk_elasticache.types.service_update_status_list.ServiceUpdateStatusList"
    ]
    """<p>The status of the service update</p>"""
    service_update_time_range: NotRequired[
        "aws_sdk_elasticache.types.time_range_filter.TimeRangeFilter"
    ]
    """<p>The range of time specified to search for service updates that are in available status</p>"""
    update_action_status: NotRequired[
        "aws_sdk_elasticache.types.update_action_status_list.UpdateActionStatusList"
    ]
    """<p>The status of the update action.</p>"""
    show_node_level_update_status: NotRequired[
        "aws_sdk_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>Dictates whether to include node level update status in the response </p>"""
    max_records: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response</p>"""
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeUpdateActionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "service_update_name" in value:
        pairs.append((f"{prefix}.ServiceUpdateName", str(value["service_update_name"])))
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
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "service_update_status" in value:
        import aws_sdk_elasticache.types.service_update_status_list

        aws_sdk_elasticache.types.service_update_status_list.serialize_query(
            value["service_update_status"], pairs, f"{prefix}.ServiceUpdateStatus"
        )
    if "service_update_time_range" in value:
        import aws_sdk_elasticache.types.time_range_filter

        aws_sdk_elasticache.types.time_range_filter.serialize_query(
            value["service_update_time_range"],
            pairs,
            f"{prefix}.ServiceUpdateTimeRange",
        )
    if "update_action_status" in value:
        import aws_sdk_elasticache.types.update_action_status_list

        aws_sdk_elasticache.types.update_action_status_list.serialize_query(
            value["update_action_status"], pairs, f"{prefix}.UpdateActionStatus"
        )
    if "show_node_level_update_status" in value:
        pairs.append(
            (
                f"{prefix}.ShowNodeLevelUpdateStatus",
                "true" if value["show_node_level_update_status"] else "false",
            )
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeUpdateActionsMessage:
    out: DescribeUpdateActionsMessage = {}  # type: ignore[typeddict-item]
    child_service_update_name = el.find("ServiceUpdateName")
    if child_service_update_name is not None:
        out["service_update_name"] = str(child_service_update_name.text or "")
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
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_service_update_status = el.find("ServiceUpdateStatus")
    if child_service_update_status is not None:
        import aws_sdk_elasticache.types.service_update_status_list

        out["service_update_status"] = (
            aws_sdk_elasticache.types.service_update_status_list.deserialize_query(
                child_service_update_status
            )
        )
    child_service_update_time_range = el.find("ServiceUpdateTimeRange")
    if child_service_update_time_range is not None:
        import aws_sdk_elasticache.types.time_range_filter

        out["service_update_time_range"] = (
            aws_sdk_elasticache.types.time_range_filter.deserialize_query(
                child_service_update_time_range
            )
        )
    child_update_action_status = el.find("UpdateActionStatus")
    if child_update_action_status is not None:
        import aws_sdk_elasticache.types.update_action_status_list

        out["update_action_status"] = (
            aws_sdk_elasticache.types.update_action_status_list.deserialize_query(
                child_update_action_status
            )
        )
    child_show_node_level_update_status = el.find("ShowNodeLevelUpdateStatus")
    if child_show_node_level_update_status is not None:
        out["show_node_level_update_status"] = (
            child_show_node_level_update_status.text or ""
        ).lower() == "true"
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
