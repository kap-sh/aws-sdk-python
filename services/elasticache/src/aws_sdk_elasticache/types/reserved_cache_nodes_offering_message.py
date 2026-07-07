"""Generated from Smithy shape ``com.amazonaws.elasticache#ReservedCacheNodesOfferingMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.reserved_cache_nodes_offering_list
    import aws_sdk_elasticache.types.string


class ReservedCacheNodesOfferingMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    reserved_cache_nodes_offerings: NotRequired[
        "aws_sdk_elasticache.types.reserved_cache_nodes_offering_list.ReservedCacheNodesOfferingList"
    ]
    """<p>A list of reserved cache node offerings. Each element in the list contains detailed information about one offering.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedCacheNodesOfferingMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "reserved_cache_nodes_offerings" in value:
        import aws_sdk_elasticache.types.reserved_cache_nodes_offering_list

        aws_sdk_elasticache.types.reserved_cache_nodes_offering_list.serialize_query(
            value["reserved_cache_nodes_offerings"],
            pairs,
            f"{prefix}.ReservedCacheNodesOfferings",
        )


def deserialize_query(el: Element) -> ReservedCacheNodesOfferingMessage:
    out: ReservedCacheNodesOfferingMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_cache_nodes_offerings = el.find("ReservedCacheNodesOfferings")
    if child_reserved_cache_nodes_offerings is not None:
        import aws_sdk_elasticache.types.reserved_cache_nodes_offering_list

        out["reserved_cache_nodes_offerings"] = (
            aws_sdk_elasticache.types.reserved_cache_nodes_offering_list.deserialize_query(
                child_reserved_cache_nodes_offerings
            )
        )
    return out
