"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaInsightsPipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline


class CreateMediaInsightsPipelineResponse(TypedDict, closed=True):
    media_insights_pipeline: "capo_chime_sdk_media_pipelines.types.media_insights_pipeline.MediaInsightsPipeline"
    """<p>The media insights pipeline object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaInsightsPipelineResponse) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline

    out["MediaInsightsPipeline"] = (
        capo_chime_sdk_media_pipelines.types.media_insights_pipeline.serialize_json(
            value["media_insights_pipeline"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateMediaInsightsPipelineResponse:
    out: CreateMediaInsightsPipelineResponse = {}  # type: ignore[typeddict-item]
    if "MediaInsightsPipeline" in data:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline

        out["media_insights_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline.deserialize_json(
                data["MediaInsightsPipeline"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMediaInsightsPipelineResponse.media_insights_pipeline required"
        )
    return out
