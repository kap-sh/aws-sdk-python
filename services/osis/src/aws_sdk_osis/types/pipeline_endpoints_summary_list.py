"""Generated from Smithy shape ``com.amazonaws.osis#PipelineEndpointsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_endpoint

PipelineEndpointsSummaryList: TypeAlias = list[
    "aws_sdk_osis.types.pipeline_endpoint.PipelineEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineEndpointsSummaryList) -> list:
    import aws_sdk_osis.types.pipeline_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_osis.types.pipeline_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineEndpointsSummaryList:
    import aws_sdk_osis.types.pipeline_endpoint

    out: PipelineEndpointsSummaryList = []
    for item in data:
        out.append(aws_sdk_osis.types.pipeline_endpoint.deserialize_json(item))
    return out
