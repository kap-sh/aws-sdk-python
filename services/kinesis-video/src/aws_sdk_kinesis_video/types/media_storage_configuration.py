"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MediaStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.media_storage_configuration_status
    import aws_sdk_kinesis_video.types.resource_arn


class MediaStorageConfiguration(TypedDict, closed=True):
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream. </p>"""
    status: "aws_sdk_kinesis_video.types.media_storage_configuration_status.MediaStorageConfigurationStatus"
    """<p>The status of the media storage configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStorageConfiguration) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import aws_sdk_kinesis_video.types.media_storage_configuration_status

    out["Status"] = (
        aws_sdk_kinesis_video.types.media_storage_configuration_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaStorageConfiguration:
    out: MediaStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "Status" in data:
        import aws_sdk_kinesis_video.types.media_storage_configuration_status

        out["status"] = (
            aws_sdk_kinesis_video.types.media_storage_configuration_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("MediaStorageConfiguration.status required")
    return out
