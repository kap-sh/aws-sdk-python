"""Generated from Smithy shape ``com.amazonaws.elasticache#ReservedCacheNodesOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.reserved_cache_nodes_offering

ReservedCacheNodesOfferingList: TypeAlias = list[
    "aws_sdk_elasticache.types.reserved_cache_nodes_offering.ReservedCacheNodesOffering"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedCacheNodesOfferingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.reserved_cache_nodes_offering

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.reserved_cache_nodes_offering.serialize_query(
            item, pairs, f"{prefix}.ReservedCacheNodesOffering.{n}"
        )


def deserialize_query(el: Element) -> ReservedCacheNodesOfferingList:
    import aws_sdk_elasticache.types.reserved_cache_nodes_offering

    out: ReservedCacheNodesOfferingList = []
    for child in el.findall("ReservedCacheNodesOffering"):
        out.append(
            aws_sdk_elasticache.types.reserved_cache_nodes_offering.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ReservedCacheNodesOfferingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.reserved_cache_nodes_offering

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.reserved_cache_nodes_offering.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReservedCacheNodesOfferingList:
    import aws_sdk_elasticache.types.reserved_cache_nodes_offering

    out: ReservedCacheNodesOfferingList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.reserved_cache_nodes_offering.deserialize_query(
                child
            )
        )
    return out
