"""Generated from Smithy shape ``com.amazonaws.osis#PipelineEndpointIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_osis.types.pipeline_endpoint_id

PipelineEndpointIdsList: TypeAlias = list[
    "capo_osis.types.pipeline_endpoint_id.PipelineEndpointId"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineEndpointIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> PipelineEndpointIdsList:
    return list(data)
