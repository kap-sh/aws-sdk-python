"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DestinationPortMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_destination_traffic_state
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.ip_address_type
    import aws_sdk_global_accelerator.types.socket_address
    import aws_sdk_global_accelerator.types.socket_addresses


class DestinationPortMapping(TypedDict):
    accelerator_arn: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the custom routing accelerator that you have port mappings for.</p>"""
    accelerator_socket_addresses: NotRequired[
        "aws_sdk_global_accelerator.types.socket_addresses.SocketAddresses"
    ]
    """<p>The IP address/port combinations (sockets) that map to a given destination socket address.</p>"""
    endpoint_group_arn: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""
    endpoint_id: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The ID for the virtual private cloud (VPC) subnet.</p>"""
    endpoint_group_region: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Web Services Region for the endpoint group.</p>"""
    destination_socket_address: NotRequired[
        "aws_sdk_global_accelerator.types.socket_address.SocketAddress"
    ]
    """<p>The endpoint IP address/port combination for traffic received on the accelerator socket address.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_global_accelerator.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type that an accelerator supports. For a custom routing accelerator, the value must be IPV4.</p>"""
    destination_traffic_state: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_destination_traffic_state.CustomRoutingDestinationTrafficState"
    ]
    """<p>Indicates whether or not a port mapping destination can receive traffic. The value is either ALLOW, if traffic is allowed to the destination, or DENY, if traffic is not allowed to the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationPortMapping) -> dict:
    out: dict = {}
    if "accelerator_arn" in value:
        out["AcceleratorArn"] = value["accelerator_arn"]
    if "accelerator_socket_addresses" in value:
        import aws_sdk_global_accelerator.types.socket_addresses

        out["AcceleratorSocketAddresses"] = (
            aws_sdk_global_accelerator.types.socket_addresses.serialize_aws_json_1_1(
                value["accelerator_socket_addresses"]
            )
        )
    if "endpoint_group_arn" in value:
        out["EndpointGroupArn"] = value["endpoint_group_arn"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "endpoint_group_region" in value:
        out["EndpointGroupRegion"] = value["endpoint_group_region"]
    if "destination_socket_address" in value:
        import aws_sdk_global_accelerator.types.socket_address

        out["DestinationSocketAddress"] = (
            aws_sdk_global_accelerator.types.socket_address.serialize_aws_json_1_1(
                value["destination_socket_address"]
            )
        )
    if "ip_address_type" in value:
        import aws_sdk_global_accelerator.types.ip_address_type

        out["IpAddressType"] = (
            aws_sdk_global_accelerator.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
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


def deserialize_aws_json_1_1(data: dict) -> DestinationPortMapping:
    out: DestinationPortMapping = {}  # type: ignore[typeddict-item]
    if "AcceleratorArn" in data:
        out["accelerator_arn"] = data["AcceleratorArn"]
    if "AcceleratorSocketAddresses" in data:
        import aws_sdk_global_accelerator.types.socket_addresses

        out["accelerator_socket_addresses"] = (
            aws_sdk_global_accelerator.types.socket_addresses.deserialize_aws_json_1_1(
                data["AcceleratorSocketAddresses"]
            )
        )
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "EndpointGroupRegion" in data:
        out["endpoint_group_region"] = data["EndpointGroupRegion"]
    if "DestinationSocketAddress" in data:
        import aws_sdk_global_accelerator.types.socket_address

        out["destination_socket_address"] = (
            aws_sdk_global_accelerator.types.socket_address.deserialize_aws_json_1_1(
                data["DestinationSocketAddress"]
            )
        )
    if "IpAddressType" in data:
        import aws_sdk_global_accelerator.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_global_accelerator.types.ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
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
