"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexProgramPipelineDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class MultiplexProgramPipelineDetail(TypedDict, closed=True):
    active_channel_pipeline: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Identifies the channel pipeline that is currently active for the pipeline (identified by PipelineId) in the multiplex."""
    pipeline_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Identifies a specific pipeline in the multiplex."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexProgramPipelineDetail) -> dict:
    out: dict = {}
    if "active_channel_pipeline" in value:
        out["activeChannelPipeline"] = value["active_channel_pipeline"]
    if "pipeline_id" in value:
        out["pipelineId"] = value["pipeline_id"]
    return out


def deserialize_json(data: dict) -> MultiplexProgramPipelineDetail:
    out: MultiplexProgramPipelineDetail = {}  # type: ignore[typeddict-item]
    if "activeChannelPipeline" in data:
        out["active_channel_pipeline"] = data["activeChannelPipeline"]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    return out
