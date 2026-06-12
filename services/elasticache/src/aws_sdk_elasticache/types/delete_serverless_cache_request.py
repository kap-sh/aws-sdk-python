"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteServerlessCacheRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class DeleteServerlessCacheRequest(TypedDict):
    serverless_cache_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The identifier of the serverless cache to be deleted.</p>"""
    final_snapshot_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Name of the final snapshot to be taken before the serverless cache is deleted. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL, i.e. a final snapshot is not taken.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServerlessCacheRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "serverless_cache_name" in value:
        pairs.append(
            (f"{prefix}.ServerlessCacheName", str(value["serverless_cache_name"]))
        )
    if "final_snapshot_name" in value:
        pairs.append((f"{prefix}.FinalSnapshotName", str(value["final_snapshot_name"])))


def deserialize_query(el: Element) -> DeleteServerlessCacheRequest:
    out: DeleteServerlessCacheRequest = {}  # type: ignore[typeddict-item]
    child_serverless_cache_name = el.find("ServerlessCacheName")
    if child_serverless_cache_name is not None:
        out["serverless_cache_name"] = str(child_serverless_cache_name.text or "")
    child_final_snapshot_name = el.find("FinalSnapshotName")
    if child_final_snapshot_name is not None:
        out["final_snapshot_name"] = str(child_final_snapshot_name.text or "")
    return out
