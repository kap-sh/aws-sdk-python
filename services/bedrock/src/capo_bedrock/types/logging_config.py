"""Generated from Smithy shape ``com.amazonaws.bedrock#LoggingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.cloud_watch_config
    import capo_bedrock.types.s3_config


class LoggingConfig(TypedDict, closed=True):
    cloud_watch_config: NotRequired[
        "capo_bedrock.types.cloud_watch_config.CloudWatchConfig"
    ]
    """<p>CloudWatch logging configuration.</p>"""
    s3_config: NotRequired["capo_bedrock.types.s3_config.S3Config"]
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
        import capo_bedrock.types.cloud_watch_config

        out["cloudWatchConfig"] = capo_bedrock.types.cloud_watch_config.serialize_json(
            value["cloud_watch_config"]
        )
    if "s3_config" in value:
        import capo_bedrock.types.s3_config

        out["s3Config"] = capo_bedrock.types.s3_config.serialize_json(
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
    if data.get("cloudWatchConfig") is not None:
        import capo_bedrock.types.cloud_watch_config

        out["cloud_watch_config"] = (
            capo_bedrock.types.cloud_watch_config.deserialize_json(
                data["cloudWatchConfig"]
            )
        )
    if data.get("s3Config") is not None:
        import capo_bedrock.types.s3_config

        out["s3_config"] = capo_bedrock.types.s3_config.deserialize_json(
            data["s3Config"]
        )
    if data.get("textDataDeliveryEnabled") is not None:
        out["text_data_delivery_enabled"] = data["textDataDeliveryEnabled"]
    if data.get("imageDataDeliveryEnabled") is not None:
        out["image_data_delivery_enabled"] = data["imageDataDeliveryEnabled"]
    if data.get("embeddingDataDeliveryEnabled") is not None:
        out["embedding_data_delivery_enabled"] = data["embeddingDataDeliveryEnabled"]
    if data.get("videoDataDeliveryEnabled") is not None:
        out["video_data_delivery_enabled"] = data["videoDataDeliveryEnabled"]
    if data.get("audioDataDeliveryEnabled") is not None:
        out["audio_data_delivery_enabled"] = data["audioDataDeliveryEnabled"]
    return out
