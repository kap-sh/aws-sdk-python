"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaConcatenationPipelineResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline


class CreateMediaConcatenationPipelineResponse(TypedDict):
    media_concatenation_pipeline: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline.MediaConcatenationPipeline"
    ]
    """<p>A media concatenation pipeline object, the ID, source type, <code>MediaPipelineARN</code>, and sink of a media concatenation pipeline object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaConcatenationPipelineResponse) -> dict:
    out: dict = {}
    if "media_concatenation_pipeline" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["MediaConcatenationPipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline.serialize_json(
                value["media_concatenation_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMediaConcatenationPipelineResponse:
    out: CreateMediaConcatenationPipelineResponse = {}  # type: ignore[typeddict-item]
    if "MediaConcatenationPipeline" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["media_concatenation_pipeline"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_concatenation_pipeline.deserialize_json(
                data["MediaConcatenationPipeline"]
            )
        )
    return out
