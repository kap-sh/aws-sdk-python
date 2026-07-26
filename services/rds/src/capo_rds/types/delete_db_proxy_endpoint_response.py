"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBProxyEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_proxy_endpoint


class DeleteDBProxyEndpointResponse(TypedDict, closed=True):
    db_proxy_endpoint: NotRequired["capo_rds.types.db_proxy_endpoint.DBProxyEndpoint"]
    """<p>The data structure representing the details of the DB proxy endpoint that you delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBProxyEndpointResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_endpoint" in value:
        import capo_rds.types.db_proxy_endpoint

        capo_rds.types.db_proxy_endpoint.serialize_query(
            value["db_proxy_endpoint"], pairs, f"{prefix}.DBProxyEndpoint"
        )


def deserialize_query(el: Element) -> DeleteDBProxyEndpointResponse:
    out: DeleteDBProxyEndpointResponse = {}  # type: ignore[typeddict-item]
    child_db_proxy_endpoint = el.find("DBProxyEndpoint")
    if child_db_proxy_endpoint is not None:
        import capo_rds.types.db_proxy_endpoint

        out["db_proxy_endpoint"] = capo_rds.types.db_proxy_endpoint.deserialize_query(
            child_db_proxy_endpoint
        )
    return out
