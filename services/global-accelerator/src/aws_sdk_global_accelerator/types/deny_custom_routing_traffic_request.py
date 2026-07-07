"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DenyCustomRoutingTrafficRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.destination_addresses
    import aws_sdk_global_accelerator.types.destination_ports
    import aws_sdk_global_accelerator.types.generic_boolean
    import aws_sdk_global_accelerator.types.generic_string


class DenyCustomRoutingTrafficRequest(TypedDict, closed=True):
    endpoint_group_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""
    endpoint_id: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID.</p>"""
    destination_addresses: NotRequired[
        "aws_sdk_global_accelerator.types.destination_addresses.DestinationAddresses"
    ]
    """<p>A list of specific Amazon EC2 instance IP addresses (destination addresses) in a subnet that you want to prevent from receiving traffic. The IP addresses must be a subset of the IP addresses allowed for the VPC subnet associated with the endpoint group.</p>"""
    destination_ports: NotRequired[
        "aws_sdk_global_accelerator.types.destination_ports.DestinationPorts"
    ]
    """<p>A list of specific Amazon EC2 instance ports (destination ports) in a subnet endpoint that you want to prevent from receiving traffic.</p>"""
    deny_all_traffic_to_endpoint: NotRequired[
        "aws_sdk_global_accelerator.types.generic_boolean.GenericBoolean"
    ]
    """<p>Indicates whether all destination IP addresses and ports for a specified VPC subnet endpoint <i>cannot</i> receive traffic from a custom routing accelerator. The value is TRUE or FALSE. </p> <p>When set to TRUE, <i>no</i> destinations in the custom routing VPC subnet can receive traffic. Note that you cannot specify destination IP addresses and ports when the value is set to TRUE.</p> <p>When set to FALSE (or not specified), you <i>must</i> specify a list of destination IP addresses that cannot receive traffic. A list of ports is optional. If you don't specify a list of ports, the ports that can accept traffic is the same as the ports configured for the endpoint group.</p> <p>The default value is FALSE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DenyCustomRoutingTrafficRequest) -> dict:
    out: dict = {}
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    out["EndpointId"] = value["endpoint_id"]
    if "destination_addresses" in value:
        import aws_sdk_global_accelerator.types.destination_addresses

        out["DestinationAddresses"] = (
            aws_sdk_global_accelerator.types.destination_addresses.serialize_aws_json_1_1(
                value["destination_addresses"]
            )
        )
    if "destination_ports" in value:
        import aws_sdk_global_accelerator.types.destination_ports

        out["DestinationPorts"] = (
            aws_sdk_global_accelerator.types.destination_ports.serialize_aws_json_1_1(
                value["destination_ports"]
            )
        )
    if "deny_all_traffic_to_endpoint" in value:
        out["DenyAllTrafficToEndpoint"] = value["deny_all_traffic_to_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DenyCustomRoutingTrafficRequest:
    out: DenyCustomRoutingTrafficRequest = {}  # type: ignore[typeddict-item]
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        raise DeserializationError(
            "DenyCustomRoutingTrafficRequest.endpoint_group_arn required"
        )
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    else:
        raise DeserializationError(
            "DenyCustomRoutingTrafficRequest.endpoint_id required"
        )
    if "DestinationAddresses" in data:
        import aws_sdk_global_accelerator.types.destination_addresses

        out["destination_addresses"] = (
            aws_sdk_global_accelerator.types.destination_addresses.deserialize_aws_json_1_1(
                data["DestinationAddresses"]
            )
        )
    if "DestinationPorts" in data:
        import aws_sdk_global_accelerator.types.destination_ports

        out["destination_ports"] = (
            aws_sdk_global_accelerator.types.destination_ports.deserialize_aws_json_1_1(
                data["DestinationPorts"]
            )
        )
    if "DenyAllTrafficToEndpoint" in data:
        out["deny_all_traffic_to_endpoint"] = data["DenyAllTrafficToEndpoint"]
    return out
