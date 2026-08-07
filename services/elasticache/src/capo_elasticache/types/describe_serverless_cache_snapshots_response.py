"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeServerlessCacheSnapshotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.serverless_cache_snapshot_list
    import capo_elasticache.types.string


class DescribeServerlessCacheSnapshotsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request to support pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by max-results. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""
    serverless_cache_snapshots: NotRequired[
        "capo_elasticache.types.serverless_cache_snapshot_list.ServerlessCacheSnapshotList"
    ]
    """<p>The serverless caches snapshots associated with a given description request. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeServerlessCacheSnapshotsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "serverless_cache_snapshots" in value:
        import capo_elasticache.types.serverless_cache_snapshot_list

        capo_elasticache.types.serverless_cache_snapshot_list.serialize_query(
            value["serverless_cache_snapshots"],
            pairs,
            f"{key_prefix}ServerlessCacheSnapshots",
        )


def deserialize_query(el: Element) -> DescribeServerlessCacheSnapshotsResponse:
    out: DescribeServerlessCacheSnapshotsResponse = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_serverless_cache_snapshots = el.find("ServerlessCacheSnapshots")
    if child_serverless_cache_snapshots is not None:
        import capo_elasticache.types.serverless_cache_snapshot_list

        out["serverless_cache_snapshots"] = (
            capo_elasticache.types.serverless_cache_snapshot_list.deserialize_query(
                child_serverless_cache_snapshots
            )
        )
    return out
