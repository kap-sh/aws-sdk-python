"""Generated from Smithy shape ``com.amazonaws.osis#StopPipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_name


class StopPipelineRequest(TypedDict):
    pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopPipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopPipelineRequest:
    out: StopPipelineRequest = {}  # type: ignore[typeddict-item]
    return out
