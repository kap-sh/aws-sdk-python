"""Generated from Smithy shape ``com.amazonaws.elasticache#PurchaseReservedCacheNodesOfferingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.reserved_cache_node


class PurchaseReservedCacheNodesOfferingResult(TypedDict, closed=True):
    reserved_cache_node: NotRequired[
        "aws_sdk_elasticache.types.reserved_cache_node.ReservedCacheNode"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: PurchaseReservedCacheNodesOfferingResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_cache_node" in value:
        import aws_sdk_elasticache.types.reserved_cache_node

        aws_sdk_elasticache.types.reserved_cache_node.serialize_query(
            value["reserved_cache_node"], pairs, f"{prefix}.ReservedCacheNode"
        )


def deserialize_query(el: Element) -> PurchaseReservedCacheNodesOfferingResult:
    out: PurchaseReservedCacheNodesOfferingResult = {}  # type: ignore[typeddict-item]
    child_reserved_cache_node = el.find("ReservedCacheNode")
    if child_reserved_cache_node is not None:
        import aws_sdk_elasticache.types.reserved_cache_node

        out["reserved_cache_node"] = (
            aws_sdk_elasticache.types.reserved_cache_node.deserialize_query(
                child_reserved_cache_node
            )
        )
    return out
