"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.boolean
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.constrained_string_list
    import aws_sdk_networkmanager.types.core_network_policy_document
    import aws_sdk_networkmanager.types.external_region_code_list
    import aws_sdk_networkmanager.types.long
    import aws_sdk_networkmanager.types.routing_policy_association_details_list
    import aws_sdk_networkmanager.types.routing_policy_direction
    import aws_sdk_networkmanager.types.service_insertion_action_list


class CoreNetworkChangeValues(TypedDict, closed=True):
    segment_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The names of the segments in a core network.</p>"""
    network_function_group_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The network function group name if the change event is associated with a network function group.</p>"""
    edge_locations: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    ]
    """<p>The Regions where edges are located in a core network. </p>"""
    asn: NotRequired["aws_sdk_networkmanager.types.long.Long"]
    """<p>The ASN of a core network.</p>"""
    cidr: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The IP addresses used for a core network.</p>"""
    destination_identifier: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the destination.</p>"""
    inside_cidr_blocks: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The inside IP addresses used for core network change values.</p>"""
    shared_segments: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The shared segments for a core network change value. </p>"""
    service_insertion_actions: NotRequired[
        "aws_sdk_networkmanager.types.service_insertion_action_list.ServiceInsertionActionList"
    ]
    """<p>Describes the service insertion action. </p>"""
    vpn_ecmp_support: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether Equal Cost Multipath (ECMP) is enabled for the core network.</p>"""
    dns_support: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether public DNS support is supported. The default is <code>true</code>. </p>"""
    security_group_referencing_support: "aws_sdk_networkmanager.types.boolean.Boolean"
    """<p>Indicates whether security group referencing is enabled for the core network.</p>"""
    routing_policy_direction: NotRequired[
        "aws_sdk_networkmanager.types.routing_policy_direction.RoutingPolicyDirection"
    ]
    """<p>The routing policy direction (inbound/outbound) in a core network change event.</p>"""
    routing_policy: NotRequired[
        "aws_sdk_networkmanager.types.core_network_policy_document.CoreNetworkPolicyDocument"
    ]
    """<p>The routing policy configuration in the core network change values.</p>"""
    peer_edge_locations: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    ]
    """<p>The edge locations of peers in the core network change values.</p>"""
    attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The attachment identifier in the core network change values.</p>"""
    routing_policy_association_details: NotRequired[
        "aws_sdk_networkmanager.types.routing_policy_association_details_list.RoutingPolicyAssociationDetailsList"
    ]
    """<p>The names of the routing policies and other association details in the core network change values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeValues) -> dict:
    out: dict = {}
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "network_function_group_name" in value:
        out["NetworkFunctionGroupName"] = value["network_function_group_name"]
    if "edge_locations" in value:
        import aws_sdk_networkmanager.types.external_region_code_list

        out["EdgeLocations"] = (
            aws_sdk_networkmanager.types.external_region_code_list.serialize_json(
                value["edge_locations"]
            )
        )
    if "asn" in value:
        out["Asn"] = value["asn"]
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    if "destination_identifier" in value:
        out["DestinationIdentifier"] = value["destination_identifier"]
    if "inside_cidr_blocks" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["InsideCidrBlocks"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["inside_cidr_blocks"]
            )
        )
    if "shared_segments" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["SharedSegments"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["shared_segments"]
            )
        )
    if "service_insertion_actions" in value:
        import aws_sdk_networkmanager.types.service_insertion_action_list

        out["ServiceInsertionActions"] = (
            aws_sdk_networkmanager.types.service_insertion_action_list.serialize_json(
                value["service_insertion_actions"]
            )
        )
    out["VpnEcmpSupport"] = value.get("vpn_ecmp_support", False)
    out["DnsSupport"] = value.get("dns_support", False)
    out["SecurityGroupReferencingSupport"] = value.get(
        "security_group_referencing_support", False
    )
    if "routing_policy_direction" in value:
        import aws_sdk_networkmanager.types.routing_policy_direction

        out["RoutingPolicyDirection"] = (
            aws_sdk_networkmanager.types.routing_policy_direction.serialize_json(
                value["routing_policy_direction"]
            )
        )
    if "routing_policy" in value:
        out["RoutingPolicy"] = value["routing_policy"]
    if "peer_edge_locations" in value:
        import aws_sdk_networkmanager.types.external_region_code_list

        out["PeerEdgeLocations"] = (
            aws_sdk_networkmanager.types.external_region_code_list.serialize_json(
                value["peer_edge_locations"]
            )
        )
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "routing_policy_association_details" in value:
        import aws_sdk_networkmanager.types.routing_policy_association_details_list

        out["RoutingPolicyAssociationDetails"] = (
            aws_sdk_networkmanager.types.routing_policy_association_details_list.serialize_json(
                value["routing_policy_association_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkChangeValues:
    out: CoreNetworkChangeValues = {}  # type: ignore[typeddict-item]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    if "NetworkFunctionGroupName" in data:
        out["network_function_group_name"] = data["NetworkFunctionGroupName"]
    if "EdgeLocations" in data:
        import aws_sdk_networkmanager.types.external_region_code_list

        out["edge_locations"] = (
            aws_sdk_networkmanager.types.external_region_code_list.deserialize_json(
                data["EdgeLocations"]
            )
        )
    if "Asn" in data:
        out["asn"] = data["Asn"]
    if "Cidr" in data:
        out["cidr"] = data["Cidr"]
    if "DestinationIdentifier" in data:
        out["destination_identifier"] = data["DestinationIdentifier"]
    if "InsideCidrBlocks" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["inside_cidr_blocks"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["InsideCidrBlocks"]
            )
        )
    if "SharedSegments" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["shared_segments"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["SharedSegments"]
            )
        )
    if "ServiceInsertionActions" in data:
        import aws_sdk_networkmanager.types.service_insertion_action_list

        out["service_insertion_actions"] = (
            aws_sdk_networkmanager.types.service_insertion_action_list.deserialize_json(
                data["ServiceInsertionActions"]
            )
        )
    if "VpnEcmpSupport" in data:
        out["vpn_ecmp_support"] = data["VpnEcmpSupport"]
    else:
        out["vpn_ecmp_support"] = False
    if "DnsSupport" in data:
        out["dns_support"] = data["DnsSupport"]
    else:
        out["dns_support"] = False
    if "SecurityGroupReferencingSupport" in data:
        out["security_group_referencing_support"] = data[
            "SecurityGroupReferencingSupport"
        ]
    else:
        out["security_group_referencing_support"] = False
    if "RoutingPolicyDirection" in data:
        import aws_sdk_networkmanager.types.routing_policy_direction

        out["routing_policy_direction"] = (
            aws_sdk_networkmanager.types.routing_policy_direction.deserialize_json(
                data["RoutingPolicyDirection"]
            )
        )
    if "RoutingPolicy" in data:
        out["routing_policy"] = data["RoutingPolicy"]
    if "PeerEdgeLocations" in data:
        import aws_sdk_networkmanager.types.external_region_code_list

        out["peer_edge_locations"] = (
            aws_sdk_networkmanager.types.external_region_code_list.deserialize_json(
                data["PeerEdgeLocations"]
            )
        )
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    if "RoutingPolicyAssociationDetails" in data:
        import aws_sdk_networkmanager.types.routing_policy_association_details_list

        out["routing_policy_association_details"] = (
            aws_sdk_networkmanager.types.routing_policy_association_details_list.deserialize_json(
                data["RoutingPolicyAssociationDetails"]
            )
        )
    return out
