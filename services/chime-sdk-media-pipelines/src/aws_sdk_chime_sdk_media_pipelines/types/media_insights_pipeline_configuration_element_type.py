"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfigurationElementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

MediaInsightsPipelineConfigurationElementType: TypeAlias = Literal[
    "AmazonTranscribeCallAnalyticsProcessor",
    "VoiceAnalyticsProcessor",
    "AmazonTranscribeProcessor",
    "KinesisDataStreamSink",
    "LambdaFunctionSink",
    "SqsQueueSink",
    "SnsTopicSink",
    "S3RecordingSink",
    "VoiceEnhancementSink",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AmazonTranscribeCallAnalyticsProcessor",
        "VoiceAnalyticsProcessor",
        "AmazonTranscribeProcessor",
        "KinesisDataStreamSink",
        "LambdaFunctionSink",
        "SqsQueueSink",
        "SnsTopicSink",
        "S3RecordingSink",
        "VoiceEnhancementSink",
    )
)


def serialize_json(value: MediaInsightsPipelineConfigurationElementType) -> str:
    return value


def deserialize_json(data: str) -> MediaInsightsPipelineConfigurationElementType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MediaInsightsPipelineConfigurationElementType value: {data!r}"
        )
    return cast(MediaInsightsPipelineConfigurationElementType, data)
