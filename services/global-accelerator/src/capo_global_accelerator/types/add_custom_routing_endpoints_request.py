"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AddCustomRoutingEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_endpoint_configurations
    import capo_global_accelerator.types.generic_string


class AddCustomRoutingEndpointsRequest(TypedDict, closed=True):
    endpoint_configurations: "capo_global_accelerator.types.custom_routing_endpoint_configurations.CustomRoutingEndpointConfigurations"
    """<p>The list of endpoint objects to add to a custom routing accelerator.</p>"""
    endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group for the custom routing endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddCustomRoutingEndpointsRequest) -> dict:
    out: dict = {}
    import capo_global_accelerator.types.custom_routing_endpoint_configurations

    out["EndpointConfigurations"] = (
        capo_global_accelerator.types.custom_routing_endpoint_configurations.serialize_aws_json_1_1(
            value["endpoint_configurations"]
        )
    )
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddCustomRoutingEndpointsRequest:
    out: AddCustomRoutingEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "EndpointConfigurations" in data:
        import capo_global_accelerator.types.custom_routing_endpoint_configurations

        out["endpoint_configurations"] = (
            capo_global_accelerator.types.custom_routing_endpoint_configurations.deserialize_aws_json_1_1(
                data["EndpointConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "AddCustomRoutingEndpointsRequest.endpoint_configurations required"
        )
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        raise DeserializationError(
            "AddCustomRoutingEndpointsRequest.endpoint_group_arn required"
        )
    return out
