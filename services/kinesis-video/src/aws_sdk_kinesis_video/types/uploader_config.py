"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UploaderConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.schedule_config


class UploaderConfig(TypedDict):
    schedule_config: "aws_sdk_kinesis_video.types.schedule_config.ScheduleConfig"
    """<p>The configuration that consists of the <code>ScheduleExpression</code> and the <code>DurationInMinutes</code> details that specify the scheduling to record from a camera, or local media file, onto the Edge Agent. If the <code>ScheduleConfig</code> is not provided in this <code>UploaderConfig</code>, then the Edge Agent will upload at regular intervals (every 1 hour).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploaderConfig) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_video.types.schedule_config

    out["ScheduleConfig"] = aws_sdk_kinesis_video.types.schedule_config.serialize_json(
        value["schedule_config"]
    )
    return out


def deserialize_json(data: dict) -> UploaderConfig:
    out: UploaderConfig = {}  # type: ignore[typeddict-item]
    if "ScheduleConfig" in data:
        import aws_sdk_kinesis_video.types.schedule_config

        out["schedule_config"] = (
            aws_sdk_kinesis_video.types.schedule_config.deserialize_json(
                data["ScheduleConfig"]
            )
        )
    else:
        raise DeserializationError("UploaderConfig.schedule_config required")
    return out
