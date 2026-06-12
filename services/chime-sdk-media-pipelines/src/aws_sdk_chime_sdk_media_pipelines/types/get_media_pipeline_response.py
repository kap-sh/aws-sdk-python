"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaPipelineResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline


class GetMediaPipelineResponse(TypedDict):
    media_pipeline: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_pipeline.MediaPipeline"
    ]
    """<p>The media pipeline object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaPipelineResponse) -> dict:
    out: dict = {}
    if "media_pipeline" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline

        out["MediaPipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline.serialize_json(
                value["media_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMediaPipelineResponse:
    out: GetMediaPipelineResponse = {}  # type: ignore[typeddict-item]
    if "MediaPipeline" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline

        out["media_pipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline.deserialize_json(
                data["MediaPipeline"]
            )
        )
    return out
