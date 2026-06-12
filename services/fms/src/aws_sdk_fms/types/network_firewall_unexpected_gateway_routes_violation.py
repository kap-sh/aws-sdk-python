"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallUnexpectedGatewayRoutesViolation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource_id
    import aws_sdk_fms.types.routes


class NetworkFirewallUnexpectedGatewayRoutesViolation(TypedDict):
    gateway_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>Information about the gateway ID.</p>"""
    violating_routes: NotRequired["aws_sdk_fms.types.routes.Routes"]
    """<p>The routes that are in violation.</p>"""
    route_table_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>Information about the route table.</p>"""
    vpc_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>Information about the VPC ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NetworkFirewallUnexpectedGatewayRoutesViolation,
) -> dict:
    out: dict = {}
    if "gateway_id" in value:
        out["GatewayId"] = value["gateway_id"]
    if "violating_routes" in value:
        import aws_sdk_fms.types.routes

        out["ViolatingRoutes"] = aws_sdk_fms.types.routes.serialize_aws_json_1_1(
            value["violating_routes"]
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NetworkFirewallUnexpectedGatewayRoutesViolation:
    out: NetworkFirewallUnexpectedGatewayRoutesViolation = {}  # type: ignore[typeddict-item]
    if "GatewayId" in data:
        out["gateway_id"] = data["GatewayId"]
    if "ViolatingRoutes" in data:
        import aws_sdk_fms.types.routes

        out["violating_routes"] = aws_sdk_fms.types.routes.deserialize_aws_json_1_1(
            data["ViolatingRoutes"]
        )
    if "RouteTableId" in data:
        out["route_table_id"] = data["RouteTableId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
