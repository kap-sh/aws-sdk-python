"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBProxyEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy_endpoint


class ModifyDBProxyEndpointResponse(TypedDict):
    db_proxy_endpoint: NotRequired[
        "aws_sdk_rds.types.db_proxy_endpoint.DBProxyEndpoint"
    ]
    """<p>The <code>DBProxyEndpoint</code> object representing the new settings for the DB proxy endpoint.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBProxyEndpointResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_endpoint" in value:
        import aws_sdk_rds.types.db_proxy_endpoint

        aws_sdk_rds.types.db_proxy_endpoint.serialize_query(
            value["db_proxy_endpoint"], pairs, f"{prefix}.DBProxyEndpoint"
        )


def deserialize_query(el: Element) -> ModifyDBProxyEndpointResponse:
    out: ModifyDBProxyEndpointResponse = {}  # type: ignore[typeddict-item]
    child_db_proxy_endpoint = el.find("DBProxyEndpoint")
    if child_db_proxy_endpoint is not None:
        import aws_sdk_rds.types.db_proxy_endpoint

        out["db_proxy_endpoint"] = (
            aws_sdk_rds.types.db_proxy_endpoint.deserialize_query(
                child_db_proxy_endpoint
            )
        )
    return out
