"""Generated from Smithy shape ``com.amazonaws.elasticache#PurchaseReservedCacheNodesOfferingMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.string
    import aws_sdk_elasticache.types.tag_list


class PurchaseReservedCacheNodesOfferingMessage(TypedDict):
    reserved_cache_nodes_offering_id: NotRequired[
        "aws_sdk_elasticache.types.string.String"
    ]
    """<p>The ID of the reserved cache node offering to purchase.</p> <p>Example: <code>438012d3-4052-4cc7-b2e3-8d3372e0e706</code> </p>"""
    reserved_cache_node_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>A customer-specified identifier to track this reservation.</p> <note> <p>The Reserved Cache Node ID is an unique customer-specified identifier to track this reservation. If this parameter is not specified, ElastiCache automatically generates an identifier for the reservation.</p> </note> <p>Example: myreservationID</p>"""
    cache_node_count: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of cache node instances to reserve.</p> <p>Default: <code>1</code> </p>"""
    tags: NotRequired["aws_sdk_elasticache.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PurchaseReservedCacheNodesOfferingMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_cache_nodes_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedCacheNodesOfferingId",
                str(value["reserved_cache_nodes_offering_id"]),
            )
        )
    if "reserved_cache_node_id" in value:
        pairs.append(
            (f"{prefix}.ReservedCacheNodeId", str(value["reserved_cache_node_id"]))
        )
    if "cache_node_count" in value:
        pairs.append((f"{prefix}.CacheNodeCount", str(value["cache_node_count"])))
    if "tags" in value:
        import aws_sdk_elasticache.types.tag_list

        aws_sdk_elasticache.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> PurchaseReservedCacheNodesOfferingMessage:
    out: PurchaseReservedCacheNodesOfferingMessage = {}  # type: ignore[typeddict-item]
    child_reserved_cache_nodes_offering_id = el.find("ReservedCacheNodesOfferingId")
    if child_reserved_cache_nodes_offering_id is not None:
        out["reserved_cache_nodes_offering_id"] = str(
            child_reserved_cache_nodes_offering_id.text or ""
        )
    child_reserved_cache_node_id = el.find("ReservedCacheNodeId")
    if child_reserved_cache_node_id is not None:
        out["reserved_cache_node_id"] = str(child_reserved_cache_node_id.text or "")
    child_cache_node_count = el.find("CacheNodeCount")
    if child_cache_node_count is not None:
        out["cache_node_count"] = int(child_cache_node_count.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elasticache.types.tag_list

        out["tags"] = aws_sdk_elasticache.types.tag_list.deserialize_query(child_tags)
    return out
