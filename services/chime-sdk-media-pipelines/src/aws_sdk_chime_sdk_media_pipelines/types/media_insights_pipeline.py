"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.arn
    import aws_sdk_chime_sdk_media_pipelines.types.guid_string
    import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_statuses
    import aws_sdk_chime_sdk_media_pipelines.types.media_insights_runtime_metadata
    import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status
    import aws_sdk_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration


class MediaInsightsPipeline(TypedDict, closed=True):
    media_pipeline_id: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The ID of a media insights pipeline.</p>"""
    media_pipeline_arn: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The ARN of a media insights pipeline.</p>"""
    media_insights_pipeline_configuration_arn: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"
    ]
    """<p>The ARN of a media insight pipeline's configuration settings.</p>"""
    status: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status.MediaPipelineStatus"
    ]
    """<p>The status of a media insights pipeline.</p>"""
    kinesis_video_stream_source_runtime_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration.KinesisVideoStreamSourceRuntimeConfiguration"
    ]
    """<p>The configuration settings for a Kinesis runtime video stream in a media insights pipeline.</p>"""
    media_insights_runtime_metadata: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_insights_runtime_metadata.MediaInsightsRuntimeMetadata"
    ]
    """<p>The runtime metadata of a media insights pipeline.</p>"""
    kinesis_video_stream_recording_source_runtime_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration.KinesisVideoStreamRecordingSourceRuntimeConfiguration"
    ]
    """<p>The runtime configuration settings for a Kinesis recording video stream in a media insights pipeline.</p>"""
    s3_recording_sink_runtime_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration.S3RecordingSinkRuntimeConfiguration"
    ]
    """<p>The runtime configuration of the Amazon S3 bucket that stores recordings in a media insights pipeline.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the media insights pipeline was created.</p>"""
    element_statuses: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_statuses.MediaInsightsPipelineElementStatuses"
    ]
    """<p>The statuses that the elements in a media insights pipeline can have during data processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipeline) -> dict:
    out: dict = {}
    if "media_pipeline_id" in value:
        out["MediaPipelineId"] = value["media_pipeline_id"]
    if "media_pipeline_arn" in value:
        out["MediaPipelineArn"] = value["media_pipeline_arn"]
    if "media_insights_pipeline_configuration_arn" in value:
        out["MediaInsightsPipelineConfigurationArn"] = value[
            "media_insights_pipeline_configuration_arn"
        ]
    if "status" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status

        out["Status"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status.serialize_json(
                value["status"]
            )
        )
    if "kinesis_video_stream_source_runtime_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration

        out["KinesisVideoStreamSourceRuntimeConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration.serialize_json(
                value["kinesis_video_stream_source_runtime_configuration"]
            )
        )
    if "media_insights_runtime_metadata" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_runtime_metadata

        out["MediaInsightsRuntimeMetadata"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_runtime_metadata.serialize_json(
                value["media_insights_runtime_metadata"]
            )
        )
    if "kinesis_video_stream_recording_source_runtime_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration

        out["KinesisVideoStreamRecordingSourceRuntimeConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration.serialize_json(
                value["kinesis_video_stream_recording_source_runtime_configuration"]
            )
        )
    if "s3_recording_sink_runtime_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration

        out["S3RecordingSinkRuntimeConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration.serialize_json(
                value["s3_recording_sink_runtime_configuration"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "element_statuses" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_statuses

        out["ElementStatuses"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_statuses.serialize_json(
                value["element_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaInsightsPipeline:
    out: MediaInsightsPipeline = {}  # type: ignore[typeddict-item]
    if "MediaPipelineId" in data:
        out["media_pipeline_id"] = data["MediaPipelineId"]
    if "MediaPipelineArn" in data:
        out["media_pipeline_arn"] = data["MediaPipelineArn"]
    if "MediaInsightsPipelineConfigurationArn" in data:
        out["media_insights_pipeline_configuration_arn"] = data[
            "MediaInsightsPipelineConfigurationArn"
        ]
    if "Status" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status

        out["status"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_pipeline_status.deserialize_json(
                data["Status"]
            )
        )
    if "KinesisVideoStreamSourceRuntimeConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration

        out["kinesis_video_stream_source_runtime_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_source_runtime_configuration.deserialize_json(
                data["KinesisVideoStreamSourceRuntimeConfiguration"]
            )
        )
    if "MediaInsightsRuntimeMetadata" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_runtime_metadata

        out["media_insights_runtime_metadata"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_runtime_metadata.deserialize_json(
                data["MediaInsightsRuntimeMetadata"]
            )
        )
    if "KinesisVideoStreamRecordingSourceRuntimeConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration

        out["kinesis_video_stream_recording_source_runtime_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_recording_source_runtime_configuration.deserialize_json(
                data["KinesisVideoStreamRecordingSourceRuntimeConfiguration"]
            )
        )
    if "S3RecordingSinkRuntimeConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration

        out["s3_recording_sink_runtime_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.s3_recording_sink_runtime_configuration.deserialize_json(
                data["S3RecordingSinkRuntimeConfiguration"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "ElementStatuses" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_statuses

        out["element_statuses"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_insights_pipeline_element_statuses.deserialize_json(
                data["ElementStatuses"]
            )
        )
    return out
