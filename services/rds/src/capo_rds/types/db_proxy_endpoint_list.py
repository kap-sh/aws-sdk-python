"""Generated from Smithy shape ``com.amazonaws.rds#DBProxyEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy_endpoint

DBProxyEndpointList: TypeAlias = list[
    "capo_rds.types.db_proxy_endpoint.DBProxyEndpoint"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBProxyEndpointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_proxy_endpoint

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_proxy_endpoint.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DBProxyEndpointList:
    import capo_rds.types.db_proxy_endpoint

    out: DBProxyEndpointList = []
    for child in el.findall("member"):
        out.append(capo_rds.types.db_proxy_endpoint.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBProxyEndpointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_proxy_endpoint

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_proxy_endpoint.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBProxyEndpointList:
    import capo_rds.types.db_proxy_endpoint

    out: DBProxyEndpointList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_proxy_endpoint.deserialize_query(child))
    return out
