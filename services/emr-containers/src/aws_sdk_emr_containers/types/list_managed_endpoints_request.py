"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListManagedEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.endpoint_states
    import aws_sdk_emr_containers.types.endpoint_types
    import aws_sdk_emr_containers.types.java_integer
    import aws_sdk_emr_containers.types.next_token
    import aws_sdk_emr_containers.types.resource_id_string


class ListManagedEndpointsRequest(TypedDict, closed=True):
    virtual_cluster_id: (
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    )
    """<p>The ID of the virtual cluster.</p>"""
    created_before: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>The date and time before which the endpoints are created.</p>"""
    created_after: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p> The date and time after which the endpoints are created.</p>"""
    types: NotRequired["aws_sdk_emr_containers.types.endpoint_types.EndpointTypes"]
    """<p>The types of the managed endpoints.</p>"""
    states: NotRequired["aws_sdk_emr_containers.types.endpoint_states.EndpointStates"]
    """<p>The states of the managed endpoints.</p>"""
    max_results: NotRequired["aws_sdk_emr_containers.types.java_integer.JavaInteger"]
    """<p>The maximum number of managed endpoints that can be listed.</p>"""
    next_token: NotRequired["aws_sdk_emr_containers.types.next_token.NextToken"]
    """<p> The token for the next set of managed endpoints to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedEndpointsRequest:
    out: ListManagedEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
