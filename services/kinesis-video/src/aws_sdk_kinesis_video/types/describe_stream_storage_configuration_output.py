"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DescribeStreamStorageConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name
    import aws_sdk_kinesis_video.types.stream_storage_configuration


class DescribeStreamStorageConfigurationOutput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""
    stream_storage_configuration: NotRequired[
        "aws_sdk_kinesis_video.types.stream_storage_configuration.StreamStorageConfiguration"
    ]
    """<p>The current storage configuration for the stream, including the default storage tier and other storage-related settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStreamStorageConfigurationOutput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_storage_configuration" in value:
        import aws_sdk_kinesis_video.types.stream_storage_configuration

        out["StreamStorageConfiguration"] = (
            aws_sdk_kinesis_video.types.stream_storage_configuration.serialize_json(
                value["stream_storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeStreamStorageConfigurationOutput:
    out: DescribeStreamStorageConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamStorageConfiguration" in data:
        import aws_sdk_kinesis_video.types.stream_storage_configuration

        out["stream_storage_configuration"] = (
            aws_sdk_kinesis_video.types.stream_storage_configuration.deserialize_json(
                data["StreamStorageConfiguration"]
            )
        )
    return out
