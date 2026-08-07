"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheEngineVersionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_engine_version_list
    import capo_elasticache.types.string


class CacheEngineVersionMessage(TypedDict, closed=True):
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    cache_engine_versions: NotRequired[
        "capo_elasticache.types.cache_engine_version_list.CacheEngineVersionList"
    ]
    """<p>A list of cache engine version details. Each element in the list contains detailed information about one cache engine version.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheEngineVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "cache_engine_versions" in value:
        import capo_elasticache.types.cache_engine_version_list

        capo_elasticache.types.cache_engine_version_list.serialize_query(
            value["cache_engine_versions"], pairs, f"{key_prefix}CacheEngineVersions"
        )


def deserialize_query(el: Element) -> CacheEngineVersionMessage:
    out: CacheEngineVersionMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cache_engine_versions = el.find("CacheEngineVersions")
    if child_cache_engine_versions is not None:
        import capo_elasticache.types.cache_engine_version_list

        out["cache_engine_versions"] = (
            capo_elasticache.types.cache_engine_version_list.deserialize_query(
                child_cache_engine_versions
            )
        )
    return out
