"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaInsightsPipelineConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration


class GetMediaInsightsPipelineConfigurationResponse(TypedDict):
    media_insights_pipeline_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration.MediaInsightsPipelineConfiguration"
    ]
    """<p>The requested media insights pipeline configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaInsightsPipelineConfigurationResponse) -> dict:
    out: dict = {}
    if "media_insights_pipeline_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration

        out["MediaInsightsPipelineConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration.serialize_json(
                value["media_insights_pipeline_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMediaInsightsPipelineConfigurationResponse:
    out: GetMediaInsightsPipelineConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "MediaInsightsPipelineConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration

        out["media_insights_pipeline_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration.deserialize_json(
                data["MediaInsightsPipelineConfiguration"]
            )
        )
    return out
