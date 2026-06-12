"""Generated from Smithy shape ``com.amazonaws.elasticache#ReservedCacheNodeMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.reserved_cache_node_list
    import aws_sdk_elasticache.types.string


class ReservedCacheNodeMessage(TypedDict):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    reserved_cache_nodes: NotRequired[
        "aws_sdk_elasticache.types.reserved_cache_node_list.ReservedCacheNodeList"
    ]
    """<p>A list of reserved cache nodes. Each element in the list contains detailed information about one node.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedCacheNodeMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "reserved_cache_nodes" in value:
        import aws_sdk_elasticache.types.reserved_cache_node_list

        aws_sdk_elasticache.types.reserved_cache_node_list.serialize_query(
            value["reserved_cache_nodes"], pairs, f"{prefix}.ReservedCacheNodes"
        )


def deserialize_query(el: Element) -> ReservedCacheNodeMessage:
    out: ReservedCacheNodeMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_cache_nodes = el.find("ReservedCacheNodes")
    if child_reserved_cache_nodes is not None:
        import aws_sdk_elasticache.types.reserved_cache_node_list

        out["reserved_cache_nodes"] = (
            aws_sdk_elasticache.types.reserved_cache_node_list.deserialize_query(
                child_reserved_cache_nodes
            )
        )
    return out
