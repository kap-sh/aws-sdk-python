"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeCustomRoutingEndpointGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_group


class DescribeCustomRoutingEndpointGroupResponse(TypedDict):
    endpoint_group: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_endpoint_group.CustomRoutingEndpointGroup"
    ]
    """<p>The description of an endpoint group for a custom routing accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomRoutingEndpointGroupResponse) -> dict:
    out: dict = {}
    if "endpoint_group" in value:
        import aws_sdk_global_accelerator.types.custom_routing_endpoint_group

        out["EndpointGroup"] = (
            aws_sdk_global_accelerator.types.custom_routing_endpoint_group.serialize_aws_json_1_1(
                value["endpoint_group"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomRoutingEndpointGroupResponse:
    out: DescribeCustomRoutingEndpointGroupResponse = {}  # type: ignore[typeddict-item]
    if "EndpointGroup" in data:
        import aws_sdk_global_accelerator.types.custom_routing_endpoint_group

        out["endpoint_group"] = (
            aws_sdk_global_accelerator.types.custom_routing_endpoint_group.deserialize_aws_json_1_1(
                data["EndpointGroup"]
            )
        )
    return out
