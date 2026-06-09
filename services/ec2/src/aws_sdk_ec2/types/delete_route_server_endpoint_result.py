"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteServerEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_endpoint


class DeleteRouteServerEndpointResult(TypedDict):
    route_server_endpoint: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint.RouteServerEndpoint"
    ]
    """<p>Information about the deleted route server endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteRouteServerEndpointResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_endpoint" in value:
        import aws_sdk_ec2.types.route_server_endpoint

        aws_sdk_ec2.types.route_server_endpoint.serialize_ec2_query(
            value["route_server_endpoint"], pairs, f"{prefix}.RouteServerEndpoint"
        )


def deserialize_ec2_query(el: Element) -> DeleteRouteServerEndpointResult:
    out: DeleteRouteServerEndpointResult = {}  # type: ignore[typeddict-item]
    child_route_server_endpoint = el.find("RouteServerEndpoint")
    if child_route_server_endpoint is not None:
        import aws_sdk_ec2.types.route_server_endpoint

        out["route_server_endpoint"] = (
            aws_sdk_ec2.types.route_server_endpoint.deserialize_ec2_query(
                child_route_server_endpoint
            )
        )
    return out
