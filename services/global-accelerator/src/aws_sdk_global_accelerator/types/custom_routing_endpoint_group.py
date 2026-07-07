"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingEndpointGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_destination_descriptions
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_descriptions
    import aws_sdk_global_accelerator.types.generic_string


class CustomRoutingEndpointGroup(TypedDict, closed=True):
    endpoint_group_arn: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""
    endpoint_group_region: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Web Services Region where the endpoint group is located.</p>"""
    destination_descriptions: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_destination_descriptions.CustomRoutingDestinationDescriptions"
    ]
    """<p>For a custom routing accelerator, describes the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.</p>"""
    endpoint_descriptions: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_endpoint_descriptions.CustomRoutingEndpointDescriptions"
    ]
    """<p>For a custom routing accelerator, describes the endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingEndpointGroup) -> dict:
    out: dict = {}
    if "endpoint_group_arn" in value:
        out["EndpointGroupArn"] = value["endpoint_group_arn"]
    if "endpoint_group_region" in value:
        out["EndpointGroupRegion"] = value["endpoint_group_region"]
    if "destination_descriptions" in value:
        import aws_sdk_global_accelerator.types.custom_routing_destination_descriptions

        out["DestinationDescriptions"] = (
            aws_sdk_global_accelerator.types.custom_routing_destination_descriptions.serialize_aws_json_1_1(
                value["destination_descriptions"]
            )
        )
    if "endpoint_descriptions" in value:
        import aws_sdk_global_accelerator.types.custom_routing_endpoint_descriptions

        out["EndpointDescriptions"] = (
            aws_sdk_global_accelerator.types.custom_routing_endpoint_descriptions.serialize_aws_json_1_1(
                value["endpoint_descriptions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomRoutingEndpointGroup:
    out: CustomRoutingEndpointGroup = {}  # type: ignore[typeddict-item]
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    if "EndpointGroupRegion" in data:
        out["endpoint_group_region"] = data["EndpointGroupRegion"]
    if "DestinationDescriptions" in data:
        import aws_sdk_global_accelerator.types.custom_routing_destination_descriptions

        out["destination_descriptions"] = (
            aws_sdk_global_accelerator.types.custom_routing_destination_descriptions.deserialize_aws_json_1_1(
                data["DestinationDescriptions"]
            )
        )
    if "EndpointDescriptions" in data:
        import aws_sdk_global_accelerator.types.custom_routing_endpoint_descriptions

        out["endpoint_descriptions"] = (
            aws_sdk_global_accelerator.types.custom_routing_endpoint_descriptions.deserialize_aws_json_1_1(
                data["EndpointDescriptions"]
            )
        )
    return out
