"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#UpdateMediaPipelineKinesisVideoStreamPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration_update
    import aws_sdk_chime_sdk_media_pipelines.types.non_empty_string


class UpdateMediaPipelineKinesisVideoStreamPoolRequest(TypedDict, closed=True):
    identifier: (
        "aws_sdk_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    )
    """<p>The unique identifier of the requested resource. Valid values include the name and ARN of the media pipeline Kinesis Video Stream pool.</p>"""
    stream_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration_update.KinesisVideoStreamConfigurationUpdate"
    ]
    """<p>The configuration settings for the video stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMediaPipelineKinesisVideoStreamPoolRequest) -> dict:
    out: dict = {}
    if "stream_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration_update

        out["StreamConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration_update.serialize_json(
                value["stream_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMediaPipelineKinesisVideoStreamPoolRequest:
    out: UpdateMediaPipelineKinesisVideoStreamPoolRequest = {}  # type: ignore[typeddict-item]
    if "StreamConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration_update

        out["stream_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration_update.deserialize_json(
                data["StreamConfiguration"]
            )
        )
    return out
