"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListEndpointGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_groups
    import capo_global_accelerator.types.generic_string


class ListEndpointGroupsResponse(TypedDict, closed=True):
    endpoint_groups: NotRequired[
        "capo_global_accelerator.types.endpoint_groups.EndpointGroups"
    ]
    """<p>The list of the endpoint groups associated with a listener.</p>"""
    next_token: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointGroupsResponse) -> dict:
    out: dict = {}
    if "endpoint_groups" in value:
        import capo_global_accelerator.types.endpoint_groups

        out["EndpointGroups"] = (
            capo_global_accelerator.types.endpoint_groups.serialize_aws_json_1_1(
                value["endpoint_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointGroupsResponse:
    out: ListEndpointGroupsResponse = {}  # type: ignore[typeddict-item]
    if "EndpointGroups" in data:
        import capo_global_accelerator.types.endpoint_groups

        out["endpoint_groups"] = (
            capo_global_accelerator.types.endpoint_groups.deserialize_aws_json_1_1(
                data["EndpointGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
