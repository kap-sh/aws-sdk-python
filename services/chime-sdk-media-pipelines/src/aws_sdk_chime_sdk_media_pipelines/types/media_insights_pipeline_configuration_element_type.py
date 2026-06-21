"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfigurationElementType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: MediaInsightsPipelineConfigurationElementType) -> str:
    return value


def deserialize_json(data: str) -> MediaInsightsPipelineConfigurationElementType:
    return cast(MediaInsightsPipelineConfigurationElementType, data)
