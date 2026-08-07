"""Generated from Smithy shape ``com.amazonaws.elasticache#ReservedCacheNodeMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.reserved_cache_node_list
    import capo_elasticache.types.string


class ReservedCacheNodeMessage(TypedDict, closed=True):
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    reserved_cache_nodes: NotRequired[
        "capo_elasticache.types.reserved_cache_node_list.ReservedCacheNodeList"
    ]
    """<p>A list of reserved cache nodes. Each element in the list contains detailed information about one node.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedCacheNodeMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "reserved_cache_nodes" in value:
        import capo_elasticache.types.reserved_cache_node_list

        capo_elasticache.types.reserved_cache_node_list.serialize_query(
            value["reserved_cache_nodes"], pairs, f"{key_prefix}ReservedCacheNodes"
        )


def deserialize_query(el: Element) -> ReservedCacheNodeMessage:
    out: ReservedCacheNodeMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_cache_nodes = el.find("ReservedCacheNodes")
    if child_reserved_cache_nodes is not None:
        import capo_elasticache.types.reserved_cache_node_list

        out["reserved_cache_nodes"] = (
            capo_elasticache.types.reserved_cache_node_list.deserialize_query(
                child_reserved_cache_nodes
            )
        )
    return out
