"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfigurationElements``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element

MediaInsightsPipelineConfigurationElements: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element.MediaInsightsPipelineConfigurationElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineConfigurationElements) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaInsightsPipelineConfigurationElements:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element

    out: MediaInsightsPipelineConfigurationElements = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element.deserialize_json(
                item
            )
        )
    return out
