"""Generated from Smithy shape ``com.amazonaws.elasticache#CustomerNodeEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.customer_node_endpoint

CustomerNodeEndpointList: TypeAlias = list[
    "capo_elasticache.types.customer_node_endpoint.CustomerNodeEndpoint"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomerNodeEndpointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.customer_node_endpoint

    for n, item in enumerate(value, 1):
        capo_elasticache.types.customer_node_endpoint.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> CustomerNodeEndpointList:
    import capo_elasticache.types.customer_node_endpoint

    out: CustomerNodeEndpointList = []
    for child in el.findall("member"):
        out.append(
            capo_elasticache.types.customer_node_endpoint.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CustomerNodeEndpointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.customer_node_endpoint

    for n, item in enumerate(value, 1):
        capo_elasticache.types.customer_node_endpoint.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CustomerNodeEndpointList:
    import capo_elasticache.types.customer_node_endpoint

    out: CustomerNodeEndpointList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.customer_node_endpoint.deserialize_query(child)
        )
    return out
