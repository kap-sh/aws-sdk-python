"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallUnexpectedFirewallRoutesViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.resource_id
    import capo_fms.types.routes


class NetworkFirewallUnexpectedFirewallRoutesViolation(TypedDict, closed=True):
    firewall_subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The subnet ID for the firewall.</p>"""
    violating_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The routes that are in violation.</p>"""
    route_table_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The ID of the route table.</p>"""
    firewall_endpoint: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The endpoint of the firewall.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the VPC ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NetworkFirewallUnexpectedFirewallRoutesViolation,
) -> dict:
    out: dict = {}
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "violating_routes" in value:
        import capo_fms.types.routes

        out["ViolatingRoutes"] = capo_fms.types.routes.serialize_aws_json_1_1(
            value["violating_routes"]
        )
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "firewall_endpoint" in value:
        out["FirewallEndpoint"] = value["firewall_endpoint"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NetworkFirewallUnexpectedFirewallRoutesViolation:
    out: NetworkFirewallUnexpectedFirewallRoutesViolation = {}  # type: ignore[typeddict-item]
    if "FirewallSubnetId" in data:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if "ViolatingRoutes" in data:
        import capo_fms.types.routes

        out["violating_routes"] = capo_fms.types.routes.deserialize_aws_json_1_1(
            data["ViolatingRoutes"]
        )
    if "RouteTableId" in data:
        out["route_table_id"] = data["RouteTableId"]
    if "FirewallEndpoint" in data:
        out["firewall_endpoint"] = data["FirewallEndpoint"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
