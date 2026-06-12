"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#KinesisVideoStreamPoolConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.arn
    import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_id
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_name
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_size
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_status


class KinesisVideoStreamPoolConfiguration(TypedDict):
    pool_arn: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The ARN of the video stream pool configuration.</p>"""
    pool_name: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_name.KinesisVideoStreamPoolName"
    ]
    """<p>The name of the video stream pool configuration.</p>"""
    pool_id: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_id.KinesisVideoStreamPoolId"
    ]
    """<p>The ID of the video stream pool in the configuration.</p>"""
    pool_status: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_status.KinesisVideoStreamPoolStatus"
    ]
    """<p>The status of the video stream pool in the configuration. </p>"""
    pool_size: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_size.KinesisVideoStreamPoolSize"
    ]
    """<p>The size of the video stream pool in the configuration.</p>"""
    stream_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration.KinesisVideoStreamConfiguration"
    ]
    """<p>The Kinesis video stream pool configuration object.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the configuration was created.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the configuration was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KinesisVideoStreamPoolConfiguration) -> dict:
    out: dict = {}
    if "pool_arn" in value:
        out["PoolArn"] = value["pool_arn"]
    if "pool_name" in value:
        out["PoolName"] = value["pool_name"]
    if "pool_id" in value:
        out["PoolId"] = value["pool_id"]
    if "pool_status" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_status

        out["PoolStatus"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_status.serialize_json(
                value["pool_status"]
            )
        )
    if "pool_size" in value:
        out["PoolSize"] = value["pool_size"]
    if "stream_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration

        out["StreamConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration.serialize_json(
                value["stream_configuration"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> KinesisVideoStreamPoolConfiguration:
    out: KinesisVideoStreamPoolConfiguration = {}  # type: ignore[typeddict-item]
    if "PoolArn" in data:
        out["pool_arn"] = data["PoolArn"]
    if "PoolName" in data:
        out["pool_name"] = data["PoolName"]
    if "PoolId" in data:
        out["pool_id"] = data["PoolId"]
    if "PoolStatus" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_status

        out["pool_status"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_pool_status.deserialize_json(
                data["PoolStatus"]
            )
        )
    if "PoolSize" in data:
        out["pool_size"] = data["PoolSize"]
    if "StreamConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration

        out["stream_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_configuration.deserialize_json(
                data["StreamConfiguration"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    return out
