"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBProxyEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_proxy_endpoint_name


class DeleteDBProxyEndpointRequest(TypedDict, closed=True):
    db_proxy_endpoint_name: NotRequired[
        "aws_sdk_rds.types.db_proxy_endpoint_name.DBProxyEndpointName"
    ]
    """<p>The name of the DB proxy endpoint to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBProxyEndpointRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_proxy_endpoint_name" in value:
        pairs.append(
            (f"{prefix}.DBProxyEndpointName", str(value["db_proxy_endpoint_name"]))
        )


def deserialize_query(el: Element) -> DeleteDBProxyEndpointRequest:
    out: DeleteDBProxyEndpointRequest = {}  # type: ignore[typeddict-item]
    child_db_proxy_endpoint_name = el.find("DBProxyEndpointName")
    if child_db_proxy_endpoint_name is not None:
        out["db_proxy_endpoint_name"] = str(child_db_proxy_endpoint_name.text or "")
    return out
