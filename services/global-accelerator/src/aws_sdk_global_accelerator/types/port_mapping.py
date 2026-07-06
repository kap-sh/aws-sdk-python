"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#PortMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_destination_traffic_state
    import aws_sdk_global_accelerator.types.custom_routing_protocols
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.port_number
    import aws_sdk_global_accelerator.types.socket_address


class PortMapping(TypedDict, closed=True):
    accelerator_port: NotRequired[
        "aws_sdk_global_accelerator.types.port_number.PortNumber"
    ]
    """<p>The accelerator port.</p>"""
    endpoint_group_arn: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""
    endpoint_id: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The IP address of the VPC subnet (the subnet ID).</p>"""
    destination_socket_address: NotRequired[
        "aws_sdk_global_accelerator.types.socket_address.SocketAddress"
    ]
    """<p>The EC2 instance IP address and port number in the virtual private cloud (VPC) subnet.</p>"""
    protocols: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_protocols.CustomRoutingProtocols"
    ]
    """<p>The protocols supported by the endpoint group.</p>"""
    destination_traffic_state: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_destination_traffic_state.CustomRoutingDestinationTrafficState"
    ]
    """<p>Indicates whether or not a port mapping destination can receive traffic. The value is either ALLOW, if traffic is allowed to the destination, or DENY, if traffic is not allowed to the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortMapping) -> dict:
    out: dict = {}
    if "accelerator_port" in value:
        out["AcceleratorPort"] = value["accelerator_port"]
    if "endpoint_group_arn" in value:
        out["EndpointGroupArn"] = value["endpoint_group_arn"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "destination_socket_address" in value:
        import aws_sdk_global_accelerator.types.socket_address

        out["DestinationSocketAddress"] = (
            aws_sdk_global_accelerator.types.socket_address.serialize_aws_json_1_1(
                value["destination_socket_address"]
            )
        )
    if "protocols" in value:
        import aws_sdk_global_accelerator.types.custom_routing_protocols

        out["Protocols"] = (
            aws_sdk_global_accelerator.types.custom_routing_protocols.serialize_aws_json_1_1(
                value["protocols"]
            )
        )
    if "destination_traffic_state" in value:
        import aws_sdk_global_accelerator.types.custom_routing_destination_traffic_state

        out["DestinationTrafficState"] = (
            aws_sdk_global_accelerator.types.custom_routing_destination_traffic_state.serialize_aws_json_1_1(
                value["destination_traffic_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PortMapping:
    out: PortMapping = {}  # type: ignore[typeddict-item]
    if "AcceleratorPort" in data:
        out["accelerator_port"] = data["AcceleratorPort"]
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "DestinationSocketAddress" in data:
        import aws_sdk_global_accelerator.types.socket_address

        out["destination_socket_address"] = (
            aws_sdk_global_accelerator.types.socket_address.deserialize_aws_json_1_1(
                data["DestinationSocketAddress"]
            )
        )
    if "Protocols" in data:
        import aws_sdk_global_accelerator.types.custom_routing_protocols

        out["protocols"] = (
            aws_sdk_global_accelerator.types.custom_routing_protocols.deserialize_aws_json_1_1(
                data["Protocols"]
            )
        )
    if "DestinationTrafficState" in data:
        import aws_sdk_global_accelerator.types.custom_routing_destination_traffic_state

        out["destination_traffic_state"] = (
            aws_sdk_global_accelerator.types.custom_routing_destination_traffic_state.deserialize_aws_json_1_1(
                data["DestinationTrafficState"]
            )
        )
    return out
