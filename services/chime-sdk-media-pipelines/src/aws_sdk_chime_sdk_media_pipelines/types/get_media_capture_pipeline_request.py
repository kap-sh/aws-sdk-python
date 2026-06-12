"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaCapturePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.guid_string


class GetMediaCapturePipelineRequest(TypedDict):
    media_pipeline_id: "aws_sdk_chime_sdk_media_pipelines.types.guid_string.GuidString"
    """<p>The ID of the pipeline that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaCapturePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMediaCapturePipelineRequest:
    out: GetMediaCapturePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
