"""Generated from Smithy shape ``com.amazonaws.fms#RouteHasOutOfScopeEndpointViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_id
    import aws_sdk_fms.types.routes


class RouteHasOutOfScopeEndpointViolation(TypedDict, closed=True):
    subnet_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The ID of the subnet associated with the route that violates the policy scope.</p>"""
    vpc_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The VPC ID of the route that violates the policy scope.</p>"""
    route_table_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The ID of the route table.</p>"""
    violating_routes: NotRequired["aws_sdk_fms.types.routes.Routes"]
    """<p>The list of routes that violate the route table.</p>"""
    subnet_availability_zone: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The subnet's Availability Zone.</p>"""
    subnet_availability_zone_id: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The ID of the subnet's Availability Zone.</p>"""
    current_firewall_subnet_route_table: NotRequired[
        "aws_sdk_fms.types.resource_id.ResourceId"
    ]
    """<p>The route table associated with the current firewall subnet.</p>"""
    firewall_subnet_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The ID of the firewall subnet.</p>"""
    firewall_subnet_routes: NotRequired["aws_sdk_fms.types.routes.Routes"]
    """<p>The list of firewall subnet routes.</p>"""
    internet_gateway_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The ID of the Internet Gateway.</p>"""
    current_internet_gateway_route_table: NotRequired[
        "aws_sdk_fms.types.resource_id.ResourceId"
    ]
    """<p>The current route table associated with the Internet Gateway.</p>"""
    internet_gateway_routes: NotRequired["aws_sdk_fms.types.routes.Routes"]
    """<p>The routes in the route table associated with the Internet Gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteHasOutOfScopeEndpointViolation) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "violating_routes" in value:
        import aws_sdk_fms.types.routes

        out["ViolatingRoutes"] = aws_sdk_fms.types.routes.serialize_aws_json_1_1(
            value["violating_routes"]
        )
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "subnet_availability_zone_id" in value:
        out["SubnetAvailabilityZoneId"] = value["subnet_availability_zone_id"]
    if "current_firewall_subnet_route_table" in value:
        out["CurrentFirewallSubnetRouteTable"] = value[
            "current_firewall_subnet_route_table"
        ]
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "firewall_subnet_routes" in value:
        import aws_sdk_fms.types.routes

        out["FirewallSubnetRoutes"] = aws_sdk_fms.types.routes.serialize_aws_json_1_1(
            value["firewall_subnet_routes"]
        )
    if "internet_gateway_id" in value:
        out["InternetGatewayId"] = value["internet_gateway_id"]
    if "current_internet_gateway_route_table" in value:
        out["CurrentInternetGatewayRouteTable"] = value[
            "current_internet_gateway_route_table"
        ]
    if "internet_gateway_routes" in value:
        import aws_sdk_fms.types.routes

        out["InternetGatewayRoutes"] = aws_sdk_fms.types.routes.serialize_aws_json_1_1(
            value["internet_gateway_routes"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RouteHasOutOfScopeEndpointViolation:
    out: RouteHasOutOfScopeEndpointViolation = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "RouteTableId" in data:
        out["route_table_id"] = data["RouteTableId"]
    if "ViolatingRoutes" in data:
        import aws_sdk_fms.types.routes

        out["violating_routes"] = aws_sdk_fms.types.routes.deserialize_aws_json_1_1(
            data["ViolatingRoutes"]
        )
    if "SubnetAvailabilityZone" in data:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if "SubnetAvailabilityZoneId" in data:
        out["subnet_availability_zone_id"] = data["SubnetAvailabilityZoneId"]
    if "CurrentFirewallSubnetRouteTable" in data:
        out["current_firewall_subnet_route_table"] = data[
            "CurrentFirewallSubnetRouteTable"
        ]
    if "FirewallSubnetId" in data:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if "FirewallSubnetRoutes" in data:
        import aws_sdk_fms.types.routes

        out["firewall_subnet_routes"] = (
            aws_sdk_fms.types.routes.deserialize_aws_json_1_1(
                data["FirewallSubnetRoutes"]
            )
        )
    if "InternetGatewayId" in data:
        out["internet_gateway_id"] = data["InternetGatewayId"]
    if "CurrentInternetGatewayRouteTable" in data:
        out["current_internet_gateway_route_table"] = data[
            "CurrentInternetGatewayRouteTable"
        ]
    if "InternetGatewayRoutes" in data:
        import aws_sdk_fms.types.routes

        out["internet_gateway_routes"] = (
            aws_sdk_fms.types.routes.deserialize_aws_json_1_1(
                data["InternetGatewayRoutes"]
            )
        )
    return out
