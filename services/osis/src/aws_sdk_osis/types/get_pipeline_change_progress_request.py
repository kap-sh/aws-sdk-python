"""Generated from Smithy shape ``com.amazonaws.osis#GetPipelineChangeProgressRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_name


class GetPipelineChangeProgressRequest(TypedDict):
    pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPipelineChangeProgressRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPipelineChangeProgressRequest:
    out: GetPipelineChangeProgressRequest = {}  # type: ignore[typeddict-item]
    return out
