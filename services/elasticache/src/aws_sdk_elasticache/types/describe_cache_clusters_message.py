"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeCacheClustersMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean_optional
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.string


class DescribeCacheClustersMessage(TypedDict):
    cache_cluster_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The user-supplied cluster identifier. If this parameter is specified, only information about that specific cluster is returned. This parameter isn't case sensitive.</p>"""
    max_records: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: minimum 20; maximum 100.</p>"""
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    show_cache_node_info: NotRequired[
        "aws_sdk_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>An optional flag that can be included in the <code>DescribeCacheCluster</code> request to retrieve information about the individual cache nodes.</p>"""
    show_cache_clusters_not_in_replication_groups: NotRequired[
        "aws_sdk_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>An optional flag that can be included in the <code>DescribeCacheCluster</code> request to show only nodes (API/CLI: clusters) that are not members of a replication group. In practice, this means Memcached and single node Valkey or Redis OSS clusters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeCacheClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "show_cache_node_info" in value:
        pairs.append(
            (
                f"{prefix}.ShowCacheNodeInfo",
                "true" if value["show_cache_node_info"] else "false",
            )
        )
    if "show_cache_clusters_not_in_replication_groups" in value:
        pairs.append(
            (
                f"{prefix}.ShowCacheClustersNotInReplicationGroups",
                "true"
                if value["show_cache_clusters_not_in_replication_groups"]
                else "false",
            )
        )


def deserialize_query(el: Element) -> DescribeCacheClustersMessage:
    out: DescribeCacheClustersMessage = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_show_cache_node_info = el.find("ShowCacheNodeInfo")
    if child_show_cache_node_info is not None:
        out["show_cache_node_info"] = (
            child_show_cache_node_info.text or ""
        ).lower() == "true"
    child_show_cache_clusters_not_in_replication_groups = el.find(
        "ShowCacheClustersNotInReplicationGroups"
    )
    if child_show_cache_clusters_not_in_replication_groups is not None:
        out["show_cache_clusters_not_in_replication_groups"] = (
            child_show_cache_clusters_not_in_replication_groups.text or ""
        ).lower() == "true"
    return out
