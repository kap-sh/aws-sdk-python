"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineElementStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status

MediaInsightsPipelineElementStatuses: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status.MediaInsightsPipelineElementStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineElementStatuses) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaInsightsPipelineElementStatuses:
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status

    out: MediaInsightsPipelineElementStatuses = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status.deserialize_json(
                item
            )
        )
    return out
