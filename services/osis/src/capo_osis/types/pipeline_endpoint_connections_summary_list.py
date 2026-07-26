"""Generated from Smithy shape ``com.amazonaws.osis#PipelineEndpointConnectionsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_osis.types.pipeline_endpoint_connection

PipelineEndpointConnectionsSummaryList: TypeAlias = list[
    "capo_osis.types.pipeline_endpoint_connection.PipelineEndpointConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineEndpointConnectionsSummaryList) -> list:
    import capo_osis.types.pipeline_endpoint_connection

    out: list = []
    for item in value:
        out.append(capo_osis.types.pipeline_endpoint_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineEndpointConnectionsSummaryList:
    import capo_osis.types.pipeline_endpoint_connection

    out: PipelineEndpointConnectionsSummaryList = []
    for item in data:
        out.append(capo_osis.types.pipeline_endpoint_connection.deserialize_json(item))
    return out
