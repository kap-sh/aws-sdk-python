"""Generated from Smithy shape ``com.amazonaws.osis#DeletePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_name


class DeletePipelineRequest(TypedDict):
    pipeline_name: "aws_sdk_osis.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePipelineRequest:
    out: DeletePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
