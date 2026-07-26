"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpnConnectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_vpn_connection_options_details
    import capo_securityhub.types.aws_ec2_vpn_connection_routes_list
    import capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_list
    import capo_securityhub.types.non_empty_string


class AwsEc2VpnConnectionDetails(TypedDict, closed=True):
    vpn_connection_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the VPN connection.</p>"""
    state: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current state of the VPN connection. Valid values are as follows:</p> <ul> <li> <p> <code>available</code> </p> </li> <li> <p> <code>deleted</code> </p> </li> <li> <p> <code>deleting</code> </p> </li> <li> <p> <code>pending</code> </p> </li> </ul>"""
    customer_gateway_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the customer gateway that is at your end of the VPN connection.</p>"""
    customer_gateway_configuration: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The configuration information for the VPN connection's customer gateway, in the native XML format.</p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of VPN connection.</p>"""
    vpn_gateway_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the virtual private gateway that is at the Amazon Web Services side of the VPN connection.</p>"""
    category: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The category of the VPN connection. <code>VPN</code> indicates an Amazon Web Services VPN connection. <code>VPN-Classic</code> indicates an Amazon Web Services Classic VPN connection.</p>"""
    vgw_telemetry: NotRequired[
        "capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_list.AwsEc2VpnConnectionVgwTelemetryList"
    ]
    """<p>Information about the VPN tunnel.</p>"""
    options: NotRequired[
        "capo_securityhub.types.aws_ec2_vpn_connection_options_details.AwsEc2VpnConnectionOptionsDetails"
    ]
    """<p>The VPN connection options.</p>"""
    routes: NotRequired[
        "capo_securityhub.types.aws_ec2_vpn_connection_routes_list.AwsEc2VpnConnectionRoutesList"
    ]
    """<p>The static routes that are associated with the VPN connection.</p>"""
    transit_gateway_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the transit gateway that is associated with the VPN connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpnConnectionDetails) -> dict:
    out: dict = {}
    if "vpn_connection_id" in value:
        out["VpnConnectionId"] = value["vpn_connection_id"]
    if "state" in value:
        out["State"] = value["state"]
    if "customer_gateway_id" in value:
        out["CustomerGatewayId"] = value["customer_gateway_id"]
    if "customer_gateway_configuration" in value:
        out["CustomerGatewayConfiguration"] = value["customer_gateway_configuration"]
    if "type" in value:
        out["Type"] = value["type"]
    if "vpn_gateway_id" in value:
        out["VpnGatewayId"] = value["vpn_gateway_id"]
    if "category" in value:
        out["Category"] = value["category"]
    if "vgw_telemetry" in value:
        import capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_list

        out["VgwTelemetry"] = (
            capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_list.serialize_json(
                value["vgw_telemetry"]
            )
        )
    if "options" in value:
        import capo_securityhub.types.aws_ec2_vpn_connection_options_details

        out["Options"] = (
            capo_securityhub.types.aws_ec2_vpn_connection_options_details.serialize_json(
                value["options"]
            )
        )
    if "routes" in value:
        import capo_securityhub.types.aws_ec2_vpn_connection_routes_list

        out["Routes"] = (
            capo_securityhub.types.aws_ec2_vpn_connection_routes_list.serialize_json(
                value["routes"]
            )
        )
    if "transit_gateway_id" in value:
        out["TransitGatewayId"] = value["transit_gateway_id"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpnConnectionDetails:
    out: AwsEc2VpnConnectionDetails = {}  # type: ignore[typeddict-item]
    if "VpnConnectionId" in data:
        out["vpn_connection_id"] = data["VpnConnectionId"]
    if "State" in data:
        out["state"] = data["State"]
    if "CustomerGatewayId" in data:
        out["customer_gateway_id"] = data["CustomerGatewayId"]
    if "CustomerGatewayConfiguration" in data:
        out["customer_gateway_configuration"] = data["CustomerGatewayConfiguration"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "VpnGatewayId" in data:
        out["vpn_gateway_id"] = data["VpnGatewayId"]
    if "Category" in data:
        out["category"] = data["Category"]
    if "VgwTelemetry" in data:
        import capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_list

        out["vgw_telemetry"] = (
            capo_securityhub.types.aws_ec2_vpn_connection_vgw_telemetry_list.deserialize_json(
                data["VgwTelemetry"]
            )
        )
    if "Options" in data:
        import capo_securityhub.types.aws_ec2_vpn_connection_options_details

        out["options"] = (
            capo_securityhub.types.aws_ec2_vpn_connection_options_details.deserialize_json(
                data["Options"]
            )
        )
    if "Routes" in data:
        import capo_securityhub.types.aws_ec2_vpn_connection_routes_list

        out["routes"] = (
            capo_securityhub.types.aws_ec2_vpn_connection_routes_list.deserialize_json(
                data["Routes"]
            )
        )
    if "TransitGatewayId" in data:
        out["transit_gateway_id"] = data["TransitGatewayId"]
    return out
