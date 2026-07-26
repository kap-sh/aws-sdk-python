"""Generated from Smithy shape ``com.amazonaws.osis#DeletePipelineEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_endpoint_id


class DeletePipelineEndpointRequest(TypedDict, closed=True):
    endpoint_id: "capo_osis.types.pipeline_endpoint_id.PipelineEndpointId"
    """<p>The unique identifier of the pipeline endpoint to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePipelineEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePipelineEndpointRequest:
    out: DeletePipelineEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
