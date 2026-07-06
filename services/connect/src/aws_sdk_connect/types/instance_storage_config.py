"""Generated from Smithy shape ``com.amazonaws.connect#InstanceStorageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.association_id
    import aws_sdk_connect.types.kinesis_firehose_config
    import aws_sdk_connect.types.kinesis_stream_config
    import aws_sdk_connect.types.kinesis_video_stream_config
    import aws_sdk_connect.types.s3_config
    import aws_sdk_connect.types.storage_type


class InstanceStorageConfig(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_connect.types.association_id.AssociationId"]
    """<p>The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.</p>"""
    storage_type: "aws_sdk_connect.types.storage_type.StorageType"
    """<p>A valid storage type.</p>"""
    s3_config: NotRequired["aws_sdk_connect.types.s3_config.S3Config"]
    """<p>The S3 bucket configuration.</p>"""
    kinesis_video_stream_config: NotRequired[
        "aws_sdk_connect.types.kinesis_video_stream_config.KinesisVideoStreamConfig"
    ]
    """<p>The configuration of the Kinesis video stream.</p>"""
    kinesis_stream_config: NotRequired[
        "aws_sdk_connect.types.kinesis_stream_config.KinesisStreamConfig"
    ]
    """<p>The configuration of the Kinesis data stream.</p>"""
    kinesis_firehose_config: NotRequired[
        "aws_sdk_connect.types.kinesis_firehose_config.KinesisFirehoseConfig"
    ]
    """<p>The configuration of the Kinesis Firehose delivery stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceStorageConfig) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    import aws_sdk_connect.types.storage_type

    out["StorageType"] = aws_sdk_connect.types.storage_type.serialize_json(
        value["storage_type"]
    )
    if "s3_config" in value:
        import aws_sdk_connect.types.s3_config

        out["S3Config"] = aws_sdk_connect.types.s3_config.serialize_json(
            value["s3_config"]
        )
    if "kinesis_video_stream_config" in value:
        import aws_sdk_connect.types.kinesis_video_stream_config

        out["KinesisVideoStreamConfig"] = (
            aws_sdk_connect.types.kinesis_video_stream_config.serialize_json(
                value["kinesis_video_stream_config"]
            )
        )
    if "kinesis_stream_config" in value:
        import aws_sdk_connect.types.kinesis_stream_config

        out["KinesisStreamConfig"] = (
            aws_sdk_connect.types.kinesis_stream_config.serialize_json(
                value["kinesis_stream_config"]
            )
        )
    if "kinesis_firehose_config" in value:
        import aws_sdk_connect.types.kinesis_firehose_config

        out["KinesisFirehoseConfig"] = (
            aws_sdk_connect.types.kinesis_firehose_config.serialize_json(
                value["kinesis_firehose_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceStorageConfig:
    out: InstanceStorageConfig = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "StorageType" in data:
        import aws_sdk_connect.types.storage_type

        out["storage_type"] = aws_sdk_connect.types.storage_type.deserialize_json(
            data["StorageType"]
        )
    else:
        raise DeserializationError("InstanceStorageConfig.storage_type required")
    if "S3Config" in data:
        import aws_sdk_connect.types.s3_config

        out["s3_config"] = aws_sdk_connect.types.s3_config.deserialize_json(
            data["S3Config"]
        )
    if "KinesisVideoStreamConfig" in data:
        import aws_sdk_connect.types.kinesis_video_stream_config

        out["kinesis_video_stream_config"] = (
            aws_sdk_connect.types.kinesis_video_stream_config.deserialize_json(
                data["KinesisVideoStreamConfig"]
            )
        )
    if "KinesisStreamConfig" in data:
        import aws_sdk_connect.types.kinesis_stream_config

        out["kinesis_stream_config"] = (
            aws_sdk_connect.types.kinesis_stream_config.deserialize_json(
                data["KinesisStreamConfig"]
            )
        )
    if "KinesisFirehoseConfig" in data:
        import aws_sdk_connect.types.kinesis_firehose_config

        out["kinesis_firehose_config"] = (
            aws_sdk_connect.types.kinesis_firehose_config.deserialize_json(
                data["KinesisFirehoseConfig"]
            )
        )
    return out
