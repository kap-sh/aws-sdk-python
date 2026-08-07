"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteServerlessCacheSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.serverless_cache_snapshot


class DeleteServerlessCacheSnapshotResponse(TypedDict, closed=True):
    serverless_cache_snapshot: NotRequired[
        "capo_elasticache.types.serverless_cache_snapshot.ServerlessCacheSnapshot"
    ]
    """<p>The snapshot to be deleted. Available for Valkey, Redis OSS and Serverless Memcached only.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServerlessCacheSnapshotResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "serverless_cache_snapshot" in value:
        import capo_elasticache.types.serverless_cache_snapshot

        capo_elasticache.types.serverless_cache_snapshot.serialize_query(
            value["serverless_cache_snapshot"],
            pairs,
            f"{key_prefix}ServerlessCacheSnapshot",
        )


def deserialize_query(el: Element) -> DeleteServerlessCacheSnapshotResponse:
    out: DeleteServerlessCacheSnapshotResponse = {}  # type: ignore[typeddict-item]
    child_serverless_cache_snapshot = el.find("ServerlessCacheSnapshot")
    if child_serverless_cache_snapshot is not None:
        import capo_elasticache.types.serverless_cache_snapshot

        out["serverless_cache_snapshot"] = (
            capo_elasticache.types.serverless_cache_snapshot.deserialize_query(
                child_serverless_cache_snapshot
            )
        )
    return out
