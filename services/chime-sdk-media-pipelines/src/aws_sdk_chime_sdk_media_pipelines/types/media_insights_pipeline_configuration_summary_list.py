"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary

MediaInsightsPipelineConfigurationSummaryList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary.MediaInsightsPipelineConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineConfigurationSummaryList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaInsightsPipelineConfigurationSummaryList:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary

    out: MediaInsightsPipelineConfigurationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary.deserialize_json(
                item
            )
        )
    return out
