"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamPoolSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary

KinesisVideoStreamPoolSummaryList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary.KinesisVideoStreamPoolSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamPoolSummaryList) -> list:
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> KinesisVideoStreamPoolSummaryList:
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary

    out: KinesisVideoStreamPoolSummaryList = []
    for item in data:
        out.append(
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary.deserialize_json(
                item
            )
        )
    return out
