"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ListMediaPipelineKinesisVideoStreamPoolsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary_list
    import capo_chime_sdk_media_pipelines.types.string


class ListMediaPipelineKinesisVideoStreamPoolsResponse(TypedDict, closed=True):
    kinesis_video_stream_pools: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary_list.KinesisVideoStreamPoolSummaryList"
    ]
    """<p>The list of video stream pools.</p>"""
    next_token: NotRequired["capo_chime_sdk_media_pipelines.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMediaPipelineKinesisVideoStreamPoolsResponse) -> dict:
    out: dict = {}
    if "kinesis_video_stream_pools" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary_list

        out["KinesisVideoStreamPools"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary_list.serialize_json(
                value["kinesis_video_stream_pools"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMediaPipelineKinesisVideoStreamPoolsResponse:
    out: ListMediaPipelineKinesisVideoStreamPoolsResponse = {}  # type: ignore[typeddict-item]
    if "KinesisVideoStreamPools" in data:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary_list

        out["kinesis_video_stream_pools"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_summary_list.deserialize_json(
                data["KinesisVideoStreamPools"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
