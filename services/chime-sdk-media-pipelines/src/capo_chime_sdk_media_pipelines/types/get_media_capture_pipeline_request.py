"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaCapturePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.guid_string


class GetMediaCapturePipelineRequest(TypedDict, closed=True):
    media_pipeline_id: "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    """<p>The ID of the pipeline that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaCapturePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMediaCapturePipelineRequest:
    out: GetMediaCapturePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
