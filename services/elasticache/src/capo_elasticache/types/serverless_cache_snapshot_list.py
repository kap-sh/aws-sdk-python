"""Generated from Smithy shape ``com.amazonaws.elasticache#ServerlessCacheSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.serverless_cache_snapshot

ServerlessCacheSnapshotList: TypeAlias = list[
    "capo_elasticache.types.serverless_cache_snapshot.ServerlessCacheSnapshot"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessCacheSnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.serverless_cache_snapshot

    for n, item in enumerate(value, 1):
        capo_elasticache.types.serverless_cache_snapshot.serialize_query(
            item, pairs, f"{prefix}.ServerlessCacheSnapshot.{n}"
        )


def deserialize_query(el: Element) -> ServerlessCacheSnapshotList:
    import capo_elasticache.types.serverless_cache_snapshot

    out: ServerlessCacheSnapshotList = []
    for child in el.findall("ServerlessCacheSnapshot"):
        out.append(
            capo_elasticache.types.serverless_cache_snapshot.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ServerlessCacheSnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.serverless_cache_snapshot

    for n, item in enumerate(value, 1):
        capo_elasticache.types.serverless_cache_snapshot.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ServerlessCacheSnapshotList:
    import capo_elasticache.types.serverless_cache_snapshot

    out: ServerlessCacheSnapshotList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.serverless_cache_snapshot.deserialize_query(child)
        )
    return out
