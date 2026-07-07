"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaPipelineKinesisVideoStreamPoolResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration


class GetMediaPipelineKinesisVideoStreamPoolResponse(TypedDict, closed=True):
    kinesis_video_stream_pool_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.KinesisVideoStreamPoolConfiguration"
    ]
    """<p>The video stream pool configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaPipelineKinesisVideoStreamPoolResponse) -> dict:
    out: dict = {}
    if "kinesis_video_stream_pool_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["KinesisVideoStreamPoolConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.serialize_json(
                value["kinesis_video_stream_pool_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMediaPipelineKinesisVideoStreamPoolResponse:
    out: GetMediaPipelineKinesisVideoStreamPoolResponse = {}  # type: ignore[typeddict-item]
    if "KinesisVideoStreamPoolConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["kinesis_video_stream_pool_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.deserialize_json(
                data["KinesisVideoStreamPoolConfiguration"]
            )
        )
    return out
