"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DeleteManagedEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DeleteManagedEndpointRequest(TypedDict, closed=True):
    id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the managed endpoint.</p>"""
    virtual_cluster_id: (
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    )
    """<p>The ID of the endpoint's virtual cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteManagedEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteManagedEndpointRequest:
    out: DeleteManagedEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
