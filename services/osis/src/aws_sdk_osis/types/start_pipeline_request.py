"""Generated from Smithy shape ``com.amazonaws.osis#StartPipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_name


class StartPipelineRequest(TypedDict):
    pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartPipelineRequest:
    out: StartPipelineRequest = {}  # type: ignore[typeddict-item]
    return out
