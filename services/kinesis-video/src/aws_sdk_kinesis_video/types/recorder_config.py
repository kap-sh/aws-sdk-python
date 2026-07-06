"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#RecorderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.media_source_config
    import aws_sdk_kinesis_video.types.schedule_config


class RecorderConfig(TypedDict, closed=True):
    media_source_config: (
        "aws_sdk_kinesis_video.types.media_source_config.MediaSourceConfig"
    )
    """<p>The configuration details that consist of the credentials required (<code>MediaUriSecretArn</code> and <code>MediaUriType</code>) to access the media files streamed to the camera. </p>"""
    schedule_config: NotRequired[
        "aws_sdk_kinesis_video.types.schedule_config.ScheduleConfig"
    ]
    """<p>The configuration that consists of the <code>ScheduleExpression</code> and the <code>DurationInMinutes</code> details that specify the scheduling to record from a camera, or local media file, onto the Edge Agent. If the <code>ScheduleExpression</code> attribute is not provided, then the Edge Agent will always be set to recording mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecorderConfig) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_video.types.media_source_config

    out["MediaSourceConfig"] = (
        aws_sdk_kinesis_video.types.media_source_config.serialize_json(
            value["media_source_config"]
        )
    )
    if "schedule_config" in value:
        import aws_sdk_kinesis_video.types.schedule_config

        out["ScheduleConfig"] = (
            aws_sdk_kinesis_video.types.schedule_config.serialize_json(
                value["schedule_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecorderConfig:
    out: RecorderConfig = {}  # type: ignore[typeddict-item]
    if "MediaSourceConfig" in data:
        import aws_sdk_kinesis_video.types.media_source_config

        out["media_source_config"] = (
            aws_sdk_kinesis_video.types.media_source_config.deserialize_json(
                data["MediaSourceConfig"]
            )
        )
    else:
        raise DeserializationError("RecorderConfig.media_source_config required")
    if "ScheduleConfig" in data:
        import aws_sdk_kinesis_video.types.schedule_config

        out["schedule_config"] = (
            aws_sdk_kinesis_video.types.schedule_config.deserialize_json(
                data["ScheduleConfig"]
            )
        )
    return out
