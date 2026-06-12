"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#UpdateMediaPipelineKinesisVideoStreamPoolResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration


class UpdateMediaPipelineKinesisVideoStreamPoolResponse(TypedDict):
    kinesis_video_stream_pool_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.KinesisVideoStreamPoolConfiguration"
    ]
    """<p>The video stream pool configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMediaPipelineKinesisVideoStreamPoolResponse) -> dict:
    out: dict = {}
    if "kinesis_video_stream_pool_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["KinesisVideoStreamPoolConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.serialize_json(
                value["kinesis_video_stream_pool_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMediaPipelineKinesisVideoStreamPoolResponse:
    out: UpdateMediaPipelineKinesisVideoStreamPoolResponse = {}  # type: ignore[typeddict-item]
    if "KinesisVideoStreamPoolConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration

        out["kinesis_video_stream_pool_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_configuration.deserialize_json(
                data["KinesisVideoStreamPoolConfiguration"]
            )
        )
    return out
