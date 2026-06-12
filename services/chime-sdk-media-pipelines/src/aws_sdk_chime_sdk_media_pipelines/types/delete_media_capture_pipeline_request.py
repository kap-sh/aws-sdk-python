"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#DeleteMediaCapturePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.guid_string


class DeleteMediaCapturePipelineRequest(TypedDict):
    media_pipeline_id: "aws_sdk_chime_sdk_media_pipelines.types.guid_string.GuidString"
    """<p>The ID of the media pipeline being deleted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMediaCapturePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMediaCapturePipelineRequest:
    out: DeleteMediaCapturePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
