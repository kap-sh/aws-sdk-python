"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#AddCustomRoutingEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_endpoint_descriptions
    import capo_global_accelerator.types.generic_string


class AddCustomRoutingEndpointsResponse(TypedDict, closed=True):
    endpoint_descriptions: NotRequired[
        "capo_global_accelerator.types.custom_routing_endpoint_descriptions.CustomRoutingEndpointDescriptions"
    ]
    """<p>The endpoint objects added to the custom routing accelerator.</p>"""
    endpoint_group_arn: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint group for the custom routing endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddCustomRoutingEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoint_descriptions" in value:
        import capo_global_accelerator.types.custom_routing_endpoint_descriptions

        out["EndpointDescriptions"] = (
            capo_global_accelerator.types.custom_routing_endpoint_descriptions.serialize_aws_json_1_1(
                value["endpoint_descriptions"]
            )
        )
    if "endpoint_group_arn" in value:
        out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddCustomRoutingEndpointsResponse:
    out: AddCustomRoutingEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "EndpointDescriptions" in data:
        import capo_global_accelerator.types.custom_routing_endpoint_descriptions

        out["endpoint_descriptions"] = (
            capo_global_accelerator.types.custom_routing_endpoint_descriptions.deserialize_aws_json_1_1(
                data["EndpointDescriptions"]
            )
        )
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    return out
