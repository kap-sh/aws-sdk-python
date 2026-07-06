"""Generated from Smithy shape ``com.amazonaws.bedrock#LoggingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.cloud_watch_config
    import aws_sdk_bedrock.types.s3_config


class LoggingConfig(TypedDict, closed=True):
    cloud_watch_config: NotRequired[
        "aws_sdk_bedrock.types.cloud_watch_config.CloudWatchConfig"
    ]
    """<p>CloudWatch logging configuration.</p>"""
    s3_config: NotRequired["aws_sdk_bedrock.types.s3_config.S3Config"]
    """<p>S3 configuration for storing log data.</p>"""
    text_data_delivery_enabled: NotRequired["bool"]
    """<p>Set to include text data in the log delivery.</p>"""
    image_data_delivery_enabled: NotRequired["bool"]
    """<p>Set to include image data in the log delivery.</p>"""
    embedding_data_delivery_enabled: NotRequired["bool"]
    """<p>Set to include embeddings data in the log delivery.</p>"""
    video_data_delivery_enabled: NotRequired["bool"]
    """<p>Set to include video data in the log delivery.</p>"""
    audio_data_delivery_enabled: NotRequired["bool"]
    """<p>Set to include audio data in the log delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfig) -> dict:
    out: dict = {}
    if "cloud_watch_config" in value:
        import aws_sdk_bedrock.types.cloud_watch_config

        out["cloudWatchConfig"] = (
            aws_sdk_bedrock.types.cloud_watch_config.serialize_json(
                value["cloud_watch_config"]
            )
        )
    if "s3_config" in value:
        import aws_sdk_bedrock.types.s3_config

        out["s3Config"] = aws_sdk_bedrock.types.s3_config.serialize_json(
            value["s3_config"]
        )
    if "text_data_delivery_enabled" in value:
        out["textDataDeliveryEnabled"] = value["text_data_delivery_enabled"]
    if "image_data_delivery_enabled" in value:
        out["imageDataDeliveryEnabled"] = value["image_data_delivery_enabled"]
    if "embedding_data_delivery_enabled" in value:
        out["embeddingDataDeliveryEnabled"] = value["embedding_data_delivery_enabled"]
    if "video_data_delivery_enabled" in value:
        out["videoDataDeliveryEnabled"] = value["video_data_delivery_enabled"]
    if "audio_data_delivery_enabled" in value:
        out["audioDataDeliveryEnabled"] = value["audio_data_delivery_enabled"]
    return out


def deserialize_json(data: dict) -> LoggingConfig:
    out: LoggingConfig = {}  # type: ignore[typeddict-item]
    if "cloudWatchConfig" in data:
        import aws_sdk_bedrock.types.cloud_watch_config

        out["cloud_watch_config"] = (
            aws_sdk_bedrock.types.cloud_watch_config.deserialize_json(
                data["cloudWatchConfig"]
            )
        )
    if "s3Config" in data:
        import aws_sdk_bedrock.types.s3_config

        out["s3_config"] = aws_sdk_bedrock.types.s3_config.deserialize_json(
            data["s3Config"]
        )
    if "textDataDeliveryEnabled" in data:
        out["text_data_delivery_enabled"] = data["textDataDeliveryEnabled"]
    if "imageDataDeliveryEnabled" in data:
        out["image_data_delivery_enabled"] = data["imageDataDeliveryEnabled"]
    if "embeddingDataDeliveryEnabled" in data:
        out["embedding_data_delivery_enabled"] = data["embeddingDataDeliveryEnabled"]
    if "videoDataDeliveryEnabled" in data:
        out["video_data_delivery_enabled"] = data["videoDataDeliveryEnabled"]
    if "audioDataDeliveryEnabled" in data:
        out["audio_data_delivery_enabled"] = data["audioDataDeliveryEnabled"]
    return out
