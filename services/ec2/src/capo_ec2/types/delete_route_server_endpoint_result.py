"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteServerEndpointResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_endpoint


class DeleteRouteServerEndpointResult(TypedDict, closed=True):
    route_server_endpoint: NotRequired[
        "capo_ec2.types.route_server_endpoint.RouteServerEndpoint"
    ]
    """<p>Information about the deleted route server endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteRouteServerEndpointResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_endpoint" in value:
        import capo_ec2.types.route_server_endpoint

        capo_ec2.types.route_server_endpoint.serialize_ec2_query(
            value["route_server_endpoint"], pairs, f"{key_prefix}RouteServerEndpoint"
        )


def deserialize_ec2_query(el: Element) -> DeleteRouteServerEndpointResult:
    out: DeleteRouteServerEndpointResult = {}  # type: ignore[typeddict-item]
    child_route_server_endpoint = el.find("RouteServerEndpoint")
    if child_route_server_endpoint is not None:
        import capo_ec2.types.route_server_endpoint

        out["route_server_endpoint"] = (
            capo_ec2.types.route_server_endpoint.deserialize_ec2_query(
                child_route_server_endpoint
            )
        )
    return out
