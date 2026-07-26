"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineElementStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status

MediaInsightsPipelineElementStatuses: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status.MediaInsightsPipelineElementStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineElementStatuses) -> list:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaInsightsPipelineElementStatuses:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status

    out: MediaInsightsPipelineElementStatuses = []
    for item in data:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_element_status.deserialize_json(
                item
            )
        )
    return out
