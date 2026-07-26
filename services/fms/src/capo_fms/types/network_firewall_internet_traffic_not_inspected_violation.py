"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallInternetTrafficNotInspectedViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.expected_routes
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id
    import capo_fms.types.routes


class NetworkFirewallInternetTrafficNotInspectedViolation(TypedDict, closed=True):
    subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The subnet ID.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The subnet Availability Zone.</p>"""
    route_table_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the route table ID.</p>"""
    violating_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The route or routes that are in violation.</p>"""
    is_route_table_used_in_different_az: "capo_fms.types.boolean.Boolean"
    """<p>Information about whether the route table is used in another Availability Zone.</p>"""
    current_firewall_subnet_route_table: NotRequired[
        "capo_fms.types.resource_id.ResourceId"
    ]
    """<p>Information about the subnet route table for the current firewall.</p>"""
    expected_firewall_endpoint: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The expected endpoint for the current firewall.</p>"""
    firewall_subnet_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The firewall subnet ID.</p>"""
    expected_firewall_subnet_routes: NotRequired[
        "capo_fms.types.expected_routes.ExpectedRoutes"
    ]
    """<p>The firewall subnet routes that are expected.</p>"""
    actual_firewall_subnet_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The actual firewall subnet routes.</p>"""
    internet_gateway_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The internet gateway ID.</p>"""
    current_internet_gateway_route_table: NotRequired[
        "capo_fms.types.resource_id.ResourceId"
    ]
    """<p>The current route table for the internet gateway.</p>"""
    expected_internet_gateway_routes: NotRequired[
        "capo_fms.types.expected_routes.ExpectedRoutes"
    ]
    """<p>The internet gateway routes that are expected.</p>"""
    actual_internet_gateway_routes: NotRequired["capo_fms.types.routes.Routes"]
    """<p>The actual internet gateway routes.</p>"""
    vpc_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>Information about the VPC ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: NetworkFirewallInternetTrafficNotInspectedViolation,
) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "route_table_id" in value:
        out["RouteTableId"] = value["route_table_id"]
    if "violating_routes" in value:
        import capo_fms.types.routes

        out["ViolatingRoutes"] = capo_fms.types.routes.serialize_aws_json_1_1(
            value["violating_routes"]
        )
    out["IsRouteTableUsedInDifferentAZ"] = value.get(
        "is_route_table_used_in_different_az", False
    )
    if "current_firewall_subnet_route_table" in value:
        out["CurrentFirewallSubnetRouteTable"] = value[
            "current_firewall_subnet_route_table"
        ]
    if "expected_firewall_endpoint" in value:
        out["ExpectedFirewallEndpoint"] = value["expected_firewall_endpoint"]
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "expected_firewall_subnet_routes" in value:
        import capo_fms.types.expected_routes

        out["ExpectedFirewallSubnetRoutes"] = (
            capo_fms.types.expected_routes.serialize_aws_json_1_1(
                value["expected_firewall_subnet_routes"]
            )
        )
    if "actual_firewall_subnet_routes" in value:
        import capo_fms.types.routes

        out["ActualFirewallSubnetRoutes"] = (
            capo_fms.types.routes.serialize_aws_json_1_1(
                value["actual_firewall_subnet_routes"]
            )
        )
    if "internet_gateway_id" in value:
        out["InternetGatewayId"] = value["internet_gateway_id"]
    if "current_internet_gateway_route_table" in value:
        out["CurrentInternetGatewayRouteTable"] = value[
            "current_internet_gateway_route_table"
        ]
    if "expected_internet_gateway_routes" in value:
        import capo_fms.types.expected_routes

        out["ExpectedInternetGatewayRoutes"] = (
            capo_fms.types.expected_routes.serialize_aws_json_1_1(
                value["expected_internet_gateway_routes"]
            )
        )
    if "actual_internet_gateway_routes" in value:
        import capo_fms.types.routes

        out["ActualInternetGatewayRoutes"] = (
            capo_fms.types.routes.serialize_aws_json_1_1(
                value["actual_internet_gateway_routes"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> NetworkFirewallInternetTrafficNotInspectedViolation:
    out: NetworkFirewallInternetTrafficNotInspectedViolation = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "SubnetAvailabilityZone" in data:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if "RouteTableId" in data:
        out["route_table_id"] = data["RouteTableId"]
    if "ViolatingRoutes" in data:
        import capo_fms.types.routes

        out["violating_routes"] = capo_fms.types.routes.deserialize_aws_json_1_1(
            data["ViolatingRoutes"]
        )
    if "IsRouteTableUsedInDifferentAZ" in data:
        out["is_route_table_used_in_different_az"] = data[
            "IsRouteTableUsedInDifferentAZ"
        ]
    else:
        out["is_route_table_used_in_different_az"] = False
    if "CurrentFirewallSubnetRouteTable" in data:
        out["current_firewall_subnet_route_table"] = data[
            "CurrentFirewallSubnetRouteTable"
        ]
    if "ExpectedFirewallEndpoint" in data:
        out["expected_firewall_endpoint"] = data["ExpectedFirewallEndpoint"]
    if "FirewallSubnetId" in data:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if "ExpectedFirewallSubnetRoutes" in data:
        import capo_fms.types.expected_routes

        out["expected_firewall_subnet_routes"] = (
            capo_fms.types.expected_routes.deserialize_aws_json_1_1(
                data["ExpectedFirewallSubnetRoutes"]
            )
        )
    if "ActualFirewallSubnetRoutes" in data:
        import capo_fms.types.routes

        out["actual_firewall_subnet_routes"] = (
            capo_fms.types.routes.deserialize_aws_json_1_1(
                data["ActualFirewallSubnetRoutes"]
            )
        )
    if "InternetGatewayId" in data:
        out["internet_gateway_id"] = data["InternetGatewayId"]
    if "CurrentInternetGatewayRouteTable" in data:
        out["current_internet_gateway_route_table"] = data[
            "CurrentInternetGatewayRouteTable"
        ]
    if "ExpectedInternetGatewayRoutes" in data:
        import capo_fms.types.expected_routes

        out["expected_internet_gateway_routes"] = (
            capo_fms.types.expected_routes.deserialize_aws_json_1_1(
                data["ExpectedInternetGatewayRoutes"]
            )
        )
    if "ActualInternetGatewayRoutes" in data:
        import capo_fms.types.routes

        out["actual_internet_gateway_routes"] = (
            capo_fms.types.routes.deserialize_aws_json_1_1(
                data["ActualInternetGatewayRoutes"]
            )
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
