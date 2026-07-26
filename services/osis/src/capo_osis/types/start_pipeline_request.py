"""Generated from Smithy shape ``com.amazonaws.osis#StartPipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline_name


class StartPipelineRequest(TypedDict, closed=True):
    pipeline_name: "capo_osis.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline to start.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartPipelineRequest:
    out: StartPipelineRequest = {}  # type: ignore[typeddict-item]
    return out
