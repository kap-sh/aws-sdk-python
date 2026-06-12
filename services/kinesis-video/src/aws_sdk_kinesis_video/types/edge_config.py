"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#EdgeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.deletion_config
    import aws_sdk_kinesis_video.types.hub_device_arn
    import aws_sdk_kinesis_video.types.recorder_config
    import aws_sdk_kinesis_video.types.uploader_config


class EdgeConfig(TypedDict):
    hub_device_arn: "aws_sdk_kinesis_video.types.hub_device_arn.HubDeviceArn"
    """<p>The \"<b>Internet of Things (IoT) Thing</b>\" Arn of the stream.</p>"""
    recorder_config: "aws_sdk_kinesis_video.types.recorder_config.RecorderConfig"
    """<p>The recorder configuration consists of the local <code>MediaSourceConfig</code> details, that are used as credentials to access the local media files streamed on the camera. </p>"""
    uploader_config: NotRequired[
        "aws_sdk_kinesis_video.types.uploader_config.UploaderConfig"
    ]
    """<p>The uploader configuration contains the <code>ScheduleExpression</code> details that are used to schedule upload jobs for the recorded media files from the Edge Agent to a Kinesis Video Stream.</p>"""
    deletion_config: NotRequired[
        "aws_sdk_kinesis_video.types.deletion_config.DeletionConfig"
    ]
    """<p>The deletion configuration is made up of the retention time (<code>EdgeRetentionInHours</code>) and local size configuration (<code>LocalSizeConfig</code>) details that are used to make the deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EdgeConfig) -> dict:
    out: dict = {}
    out["HubDeviceArn"] = value["hub_device_arn"]
    import aws_sdk_kinesis_video.types.recorder_config

    out["RecorderConfig"] = aws_sdk_kinesis_video.types.recorder_config.serialize_json(
        value["recorder_config"]
    )
    if "uploader_config" in value:
        import aws_sdk_kinesis_video.types.uploader_config

        out["UploaderConfig"] = (
            aws_sdk_kinesis_video.types.uploader_config.serialize_json(
                value["uploader_config"]
            )
        )
    if "deletion_config" in value:
        import aws_sdk_kinesis_video.types.deletion_config

        out["DeletionConfig"] = (
            aws_sdk_kinesis_video.types.deletion_config.serialize_json(
                value["deletion_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> EdgeConfig:
    out: EdgeConfig = {}  # type: ignore[typeddict-item]
    if "HubDeviceArn" in data:
        out["hub_device_arn"] = data["HubDeviceArn"]
    else:
        raise DeserializationError("EdgeConfig.hub_device_arn required")
    if "RecorderConfig" in data:
        import aws_sdk_kinesis_video.types.recorder_config

        out["recorder_config"] = (
            aws_sdk_kinesis_video.types.recorder_config.deserialize_json(
                data["RecorderConfig"]
            )
        )
    else:
        raise DeserializationError("EdgeConfig.recorder_config required")
    if "UploaderConfig" in data:
        import aws_sdk_kinesis_video.types.uploader_config

        out["uploader_config"] = (
            aws_sdk_kinesis_video.types.uploader_config.deserialize_json(
                data["UploaderConfig"]
            )
        )
    if "DeletionConfig" in data:
        import aws_sdk_kinesis_video.types.deletion_config

        out["deletion_config"] = (
            aws_sdk_kinesis_video.types.deletion_config.deserialize_json(
                data["DeletionConfig"]
            )
        )
    return out
