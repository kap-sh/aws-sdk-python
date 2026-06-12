"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCustomRoutingEndpointGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_endpoint_groups
    import aws_sdk_global_accelerator.types.generic_string


class ListCustomRoutingEndpointGroupsResponse(TypedDict):
    endpoint_groups: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_endpoint_groups.CustomRoutingEndpointGroups"
    ]
    """<p>The list of the endpoint groups associated with a listener for a custom routing accelerator.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCustomRoutingEndpointGroupsResponse) -> dict:
    out: dict = {}
    if "endpoint_groups" in value:
        import aws_sdk_global_accelerator.types.custom_routing_endpoint_groups

        out["EndpointGroups"] = (
            aws_sdk_global_accelerator.types.custom_routing_endpoint_groups.serialize_aws_json_1_1(
                value["endpoint_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCustomRoutingEndpointGroupsResponse:
    out: ListCustomRoutingEndpointGroupsResponse = {}  # type: ignore[typeddict-item]
    if "EndpointGroups" in data:
        import aws_sdk_global_accelerator.types.custom_routing_endpoint_groups

        out["endpoint_groups"] = (
            aws_sdk_global_accelerator.types.custom_routing_endpoint_groups.deserialize_aws_json_1_1(
                data["EndpointGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
