"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfigurationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary

MediaInsightsPipelineConfigurationSummaryList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary.MediaInsightsPipelineConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineConfigurationSummaryList) -> list:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaInsightsPipelineConfigurationSummaryList:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary

    out: MediaInsightsPipelineConfigurationSummaryList = []
    for item in data:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary.deserialize_json(
                item
            )
        )
    return out
