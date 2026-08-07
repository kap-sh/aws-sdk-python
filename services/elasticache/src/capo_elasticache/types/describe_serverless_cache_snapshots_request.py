"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeServerlessCacheSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.string


class DescribeServerlessCacheSnapshotsRequest(TypedDict, closed=True):
    serverless_cache_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of serverless cache. If this parameter is specified, only snapshots associated with that specific serverless cache are described. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    serverless_cache_snapshot_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The identifier of the serverless cache’s snapshot. If this parameter is specified, only this snapshot is described. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    snapshot_type: NotRequired["capo_elasticache.types.string.String"]
    """<p>The type of snapshot that is being described. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    next_token: NotRequired["capo_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by max-results. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    max_results: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified max-results value, a market is included in the response so that remaining results can be retrieved. Available for Valkey, Redis OSS and Serverless Memcached only.The default is 50. The Validation Constraints are a maximum of 50.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeServerlessCacheSnapshotsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{key_prefix}ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "serverless_cache_snapshot_name" in value:
        pairs.append(
            (
                f"{key_prefix}ServerlessCacheSnapshotName",
                str(value["serverless_cache_snapshot_name"]),
            )
        )
    if "snapshot_type" in value:
        pairs.append((f"{key_prefix}SnapshotType", str(value["snapshot_type"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_query(el: Element) -> DescribeServerlessCacheSnapshotsRequest:
    out: DescribeServerlessCacheSnapshotsRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_serverless_cache_snapshot_name = el.find("ServerlessCacheSnapshotName")
    if child_serverless_cache_snapshot_name is not None:
        out["serverless_cache_snapshot_name"] = str(
            child_serverless_cache_snapshot_name.text or ""
        )
    child_snapshot_type = el.find("SnapshotType")
    if child_snapshot_type is not None:
        out["snapshot_type"] = str(child_snapshot_type.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out
