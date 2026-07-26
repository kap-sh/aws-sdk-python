"""Generated from Smithy shape ``com.amazonaws.osis#GetPipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_name


class GetPipelineRequest(TypedDict, closed=True):
    pipeline_name: "capo_osis.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPipelineRequest:
    out: GetPipelineRequest = {}  # type: ignore[typeddict-item]
    return out
