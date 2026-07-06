"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#DeleteMediaPipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.guid_string


class DeleteMediaPipelineRequest(TypedDict, closed=True):
    media_pipeline_id: "aws_sdk_chime_sdk_media_pipelines.types.guid_string.GuidString"
    """<p>The ID of the media pipeline to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMediaPipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMediaPipelineRequest:
    out: DeleteMediaPipelineRequest = {}  # type: ignore[typeddict-item]
    return out
