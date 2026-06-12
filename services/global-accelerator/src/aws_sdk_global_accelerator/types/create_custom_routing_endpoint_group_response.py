"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateCustomRoutingEndpointGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_group


class CreateCustomRoutingEndpointGroupResponse(TypedDict):
    endpoint_group: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_endpoint_group.CustomRoutingEndpointGroup"
    ]
    """<p>The information about the endpoint group created for a custom routing accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomRoutingEndpointGroupResponse) -> dict:
    out: dict = {}
    if "endpoint_group" in value:
        import aws_sdk_global_accelerator.types.custom_routing_endpoint_group

        out["EndpointGroup"] = (
            aws_sdk_global_accelerator.types.custom_routing_endpoint_group.serialize_aws_json_1_1(
                value["endpoint_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomRoutingEndpointGroupResponse:
    out: CreateCustomRoutingEndpointGroupResponse = {}  # type: ignore[typeddict-item]
    if "EndpointGroup" in data:
        import aws_sdk_global_accelerator.types.custom_routing_endpoint_group

        out["endpoint_group"] = (
            aws_sdk_global_accelerator.types.custom_routing_endpoint_group.deserialize_aws_json_1_1(
                data["EndpointGroup"]
            )
        )
    return out
