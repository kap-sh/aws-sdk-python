"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaCapturePipelineSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_summary

MediaCapturePipelineSummaryList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_summary.MediaCapturePipelineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaCapturePipelineSummaryList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaCapturePipelineSummaryList:
    import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_summary

    out: MediaCapturePipelineSummaryList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_summary.deserialize_json(
                item
            )
        )
    return out
