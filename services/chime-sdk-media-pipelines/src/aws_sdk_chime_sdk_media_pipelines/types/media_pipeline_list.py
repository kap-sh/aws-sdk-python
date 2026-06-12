"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipelineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_summary

MediaPipelineList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_summary.MediaPipelineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipelineList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaPipelineList:
    import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_summary

    out: MediaPipelineList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_summary.deserialize_json(
                item
            )
        )
    return out
