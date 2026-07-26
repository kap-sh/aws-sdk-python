"""Generated from Smithy shape ``com.amazonaws.osis#StopPipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.pipeline


class StopPipelineResponse(TypedDict, closed=True):
    pipeline: NotRequired["capo_osis.types.pipeline.Pipeline"]


# --- restJson1 ser/de ---
def serialize_json(value: StopPipelineResponse) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import capo_osis.types.pipeline

        out["Pipeline"] = capo_osis.types.pipeline.serialize_json(value["pipeline"])
    return out


def deserialize_json(data: dict) -> StopPipelineResponse:
    out: StopPipelineResponse = {}  # type: ignore[typeddict-item]
    if "Pipeline" in data:
        import capo_osis.types.pipeline

        out["pipeline"] = capo_osis.types.pipeline.deserialize_json(data["Pipeline"])
    return out
