"""Generated from Smithy shape ``com.amazonaws.directconnect#DirectConnectGatewayAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.associated_core_network
    import capo_direct_connect.types.associated_gateway
    import capo_direct_connect.types.direct_connect_gateway_association_id
    import capo_direct_connect.types.direct_connect_gateway_association_state
    import capo_direct_connect.types.direct_connect_gateway_id
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.route_filter_prefix_list
    import capo_direct_connect.types.state_change_error
    import capo_direct_connect.types.virtual_gateway_id
    import capo_direct_connect.types.virtual_gateway_region


class DirectConnectGatewayAssociation(TypedDict, closed=True):
    direct_connect_gateway_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_id.DirectConnectGatewayId"
    ]
    """<p>The ID of the Direct Connect gateway.</p>"""
    direct_connect_gateway_owner_account: NotRequired[
        "capo_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The ID of the Amazon Web Services account that owns the associated gateway.</p>"""
    association_state: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_state.DirectConnectGatewayAssociationState"
    ]
    """<p>The state of the association. The following are the possible values:</p> <ul> <li> <p> <code>associating</code>: The initial state after calling <a>CreateDirectConnectGatewayAssociation</a>.</p> </li> <li> <p> <code>associated</code>: The Direct Connect gateway and virtual private gateway or transit gateway are successfully associated and ready to pass traffic.</p> </li> <li> <p> <code>disassociating</code>: The initial state after calling <a>DeleteDirectConnectGatewayAssociation</a>.</p> </li> <li> <p> <code>disassociated</code>: The virtual private gateway or transit gateway is disassociated from the Direct Connect gateway. Traffic flow between the Direct Connect gateway and virtual private gateway or transit gateway is stopped.</p> </li> <li> <p> <code>updating</code>: The CIDR blocks for the virtual private gateway or transit gateway are currently being updated. This could be new CIDR blocks added or current CIDR blocks removed.</p> </li> </ul>"""
    state_change_error: NotRequired[
        "capo_direct_connect.types.state_change_error.StateChangeError"
    ]
    """<p>The error message if the state of an object failed to advance.</p>"""
    associated_gateway: NotRequired[
        "capo_direct_connect.types.associated_gateway.AssociatedGateway"
    ]
    """<p>Information about the associated gateway.</p>"""
    association_id: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_association_id.DirectConnectGatewayAssociationId"
    ]
    """<p>The ID of the Direct Connect gateway association.</p>"""
    allowed_prefixes_to_direct_connect_gateway: NotRequired[
        "capo_direct_connect.types.route_filter_prefix_list.RouteFilterPrefixList"
    ]
    """<p>The Amazon VPC prefixes to advertise to the Direct Connect gateway.</p>"""
    associated_core_network: NotRequired[
        "capo_direct_connect.types.associated_core_network.AssociatedCoreNetwork"
    ]
    """<p>The ID of the Cloud WAN core network associated with the Direct Connect gateway attachment.</p>"""
    virtual_gateway_id: NotRequired[
        "capo_direct_connect.types.virtual_gateway_id.VirtualGatewayId"
    ]
    """<p>The ID of the virtual private gateway. Applies only to private virtual interfaces.</p>"""
    virtual_gateway_region: NotRequired[
        "capo_direct_connect.types.virtual_gateway_region.VirtualGatewayRegion"
    ]
    """<p>The Amazon Web Services Region where the virtual private gateway is located.</p>"""
    virtual_gateway_owner_account: NotRequired[
        "capo_direct_connect.types.owner_account.OwnerAccount"
    ]
    """<p>The ID of the Amazon Web Services account that owns the virtual private gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectConnectGatewayAssociation) -> dict:
    out: dict = {}
    if "direct_connect_gateway_id" in value:
        out["directConnectGatewayId"] = value["direct_connect_gateway_id"]
    if "direct_connect_gateway_owner_account" in value:
        out["directConnectGatewayOwnerAccount"] = value[
            "direct_connect_gateway_owner_account"
        ]
    if "association_state" in value:
        import capo_direct_connect.types.direct_connect_gateway_association_state

        out["associationState"] = (
            capo_direct_connect.types.direct_connect_gateway_association_state.serialize_aws_json_1_1(
                value["association_state"]
            )
        )
    if "state_change_error" in value:
        out["stateChangeError"] = value["state_change_error"]
    if "associated_gateway" in value:
        import capo_direct_connect.types.associated_gateway

        out["associatedGateway"] = (
            capo_direct_connect.types.associated_gateway.serialize_aws_json_1_1(
                value["associated_gateway"]
            )
        )
    if "association_id" in value:
        out["associationId"] = value["association_id"]
    if "allowed_prefixes_to_direct_connect_gateway" in value:
        import capo_direct_connect.types.route_filter_prefix_list

        out["allowedPrefixesToDirectConnectGateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.serialize_aws_json_1_1(
                value["allowed_prefixes_to_direct_connect_gateway"]
            )
        )
    if "associated_core_network" in value:
        import capo_direct_connect.types.associated_core_network

        out["associatedCoreNetwork"] = (
            capo_direct_connect.types.associated_core_network.serialize_aws_json_1_1(
                value["associated_core_network"]
            )
        )
    if "virtual_gateway_id" in value:
        out["virtualGatewayId"] = value["virtual_gateway_id"]
    if "virtual_gateway_region" in value:
        out["virtualGatewayRegion"] = value["virtual_gateway_region"]
    if "virtual_gateway_owner_account" in value:
        out["virtualGatewayOwnerAccount"] = value["virtual_gateway_owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DirectConnectGatewayAssociation:
    out: DirectConnectGatewayAssociation = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayId" in data:
        out["direct_connect_gateway_id"] = data["directConnectGatewayId"]
    if "directConnectGatewayOwnerAccount" in data:
        out["direct_connect_gateway_owner_account"] = data[
            "directConnectGatewayOwnerAccount"
        ]
    if "associationState" in data:
        import capo_direct_connect.types.direct_connect_gateway_association_state

        out["association_state"] = (
            capo_direct_connect.types.direct_connect_gateway_association_state.deserialize_aws_json_1_1(
                data["associationState"]
            )
        )
    if "stateChangeError" in data:
        out["state_change_error"] = data["stateChangeError"]
    if "associatedGateway" in data:
        import capo_direct_connect.types.associated_gateway

        out["associated_gateway"] = (
            capo_direct_connect.types.associated_gateway.deserialize_aws_json_1_1(
                data["associatedGateway"]
            )
        )
    if "associationId" in data:
        out["association_id"] = data["associationId"]
    if "allowedPrefixesToDirectConnectGateway" in data:
        import capo_direct_connect.types.route_filter_prefix_list

        out["allowed_prefixes_to_direct_connect_gateway"] = (
            capo_direct_connect.types.route_filter_prefix_list.deserialize_aws_json_1_1(
                data["allowedPrefixesToDirectConnectGateway"]
            )
        )
    if "associatedCoreNetwork" in data:
        import capo_direct_connect.types.associated_core_network

        out["associated_core_network"] = (
            capo_direct_connect.types.associated_core_network.deserialize_aws_json_1_1(
                data["associatedCoreNetwork"]
            )
        )
    if "virtualGatewayId" in data:
        out["virtual_gateway_id"] = data["virtualGatewayId"]
    if "virtualGatewayRegion" in data:
        out["virtual_gateway_region"] = data["virtualGatewayRegion"]
    if "virtualGatewayOwnerAccount" in data:
        out["virtual_gateway_owner_account"] = data["virtualGatewayOwnerAccount"]
    return out
