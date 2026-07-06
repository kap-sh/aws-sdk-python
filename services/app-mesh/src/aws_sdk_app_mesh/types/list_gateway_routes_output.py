"""Generated from Smithy shape ``com.amazonaws.appmesh#ListGatewayRoutesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.gateway_route_list


class ListGatewayRoutesOutput(TypedDict, closed=True):
    gateway_routes: "aws_sdk_app_mesh.types.gateway_route_list.GatewayRouteList"
    """<p>The list of existing gateway routes for the specified service mesh and virtual gateway.</p>"""
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListGatewayRoutes</code> request. When the results of a <code>ListGatewayRoutes</code> request exceed <code>limit</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayRoutesOutput) -> dict:
    out: dict = {}
    import aws_sdk_app_mesh.types.gateway_route_list

    out["gatewayRoutes"] = aws_sdk_app_mesh.types.gateway_route_list.serialize_json(
        value["gateway_routes"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewayRoutesOutput:
    out: ListGatewayRoutesOutput = {}  # type: ignore[typeddict-item]
    if "gatewayRoutes" in data:
        import aws_sdk_app_mesh.types.gateway_route_list

        out["gateway_routes"] = (
            aws_sdk_app_mesh.types.gateway_route_list.deserialize_json(
                data["gatewayRoutes"]
            )
        )
    else:
        raise DeserializationError("ListGatewayRoutesOutput.gateway_routes required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
