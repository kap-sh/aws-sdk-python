"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#UpdateMediaPipelineKinesisVideoStreamPoolResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration


class UpdateMediaPipelineKinesisVideoStreamPoolResponse(TypedDict, closed=True):
    kinesis_video_stream_pool_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.KinesisVideoStreamPoolConfiguration"
    ]
    """<p>The video stream pool configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMediaPipelineKinesisVideoStreamPoolResponse) -> dict:
    out: dict = {}
    if "kinesis_video_stream_pool_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["KinesisVideoStreamPoolConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.serialize_json(
                value["kinesis_video_stream_pool_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMediaPipelineKinesisVideoStreamPoolResponse:
    out: UpdateMediaPipelineKinesisVideoStreamPoolResponse = {}  # type: ignore[typeddict-item]
    if "KinesisVideoStreamPoolConfiguration" in data:
        import capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["kinesis_video_stream_pool_configuration"] = (
            capo_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.deserialize_json(
                data["KinesisVideoStreamPoolConfiguration"]
            )
        )
    return out
