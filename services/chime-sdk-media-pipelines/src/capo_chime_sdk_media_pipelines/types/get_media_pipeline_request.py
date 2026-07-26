"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaPipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.guid_string


class GetMediaPipelineRequest(TypedDict, closed=True):
    media_pipeline_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    """<p>The ID of the pipeline that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaPipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMediaPipelineRequest:
    out: GetMediaPipelineRequest = {}  # type: ignore[typeddict-item]
    return out
