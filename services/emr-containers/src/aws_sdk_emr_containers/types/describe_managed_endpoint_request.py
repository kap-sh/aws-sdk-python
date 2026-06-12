"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeManagedEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DescribeManagedEndpointRequest(TypedDict):
    id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>This output displays ID of the managed endpoint.</p>"""
    virtual_cluster_id: (
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    )
    """<p>The ID of the endpoint's virtual cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeManagedEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeManagedEndpointRequest:
    out: DescribeManagedEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
