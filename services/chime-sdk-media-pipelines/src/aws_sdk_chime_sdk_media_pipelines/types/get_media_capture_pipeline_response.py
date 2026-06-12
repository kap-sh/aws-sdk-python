"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaCapturePipelineResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline


class GetMediaCapturePipelineResponse(TypedDict):
    media_capture_pipeline: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline.MediaCapturePipeline"
    ]
    """<p>The media pipeline object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaCapturePipelineResponse) -> dict:
    out: dict = {}
    if "media_capture_pipeline" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["MediaCapturePipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline.serialize_json(
                value["media_capture_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMediaCapturePipelineResponse:
    out: GetMediaCapturePipelineResponse = {}  # type: ignore[typeddict-item]
    if "MediaCapturePipeline" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["media_capture_pipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline.deserialize_json(
                data["MediaCapturePipeline"]
            )
        )
    return out
