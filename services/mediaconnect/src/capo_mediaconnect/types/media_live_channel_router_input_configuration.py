"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveChannelRouterInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.media_live_channel_arn
    import capo_mediaconnect.types.media_live_channel_pipeline_id
    import capo_mediaconnect.types.media_live_transit_encryption


class MediaLiveChannelRouterInputConfiguration(TypedDict, closed=True):
    media_live_channel_arn: NotRequired[
        "capo_mediaconnect.types.media_live_channel_arn.MediaLiveChannelArn"
    ]
    """<p>The ARN of the MediaLive channel to connect to this router input.</p>"""
    media_live_pipeline_id: NotRequired[
        "capo_mediaconnect.types.media_live_channel_pipeline_id.MediaLiveChannelPipelineId"
    ]
    """<p>The index of the MediaLive pipeline to connect to this router input.</p>"""
    media_live_channel_output_name: NotRequired["str"]
    """<p>The name of the MediaLive channel output to connect to this router input.</p>"""
    source_transit_decryption: "capo_mediaconnect.types.media_live_transit_encryption.MediaLiveTransitEncryption"


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveChannelRouterInputConfiguration) -> dict:
    out: dict = {}
    if "media_live_channel_arn" in value:
        out["mediaLiveChannelArn"] = value["media_live_channel_arn"]
    if "media_live_pipeline_id" in value:
        import capo_mediaconnect.types.media_live_channel_pipeline_id

        out["mediaLivePipelineId"] = (
            capo_mediaconnect.types.media_live_channel_pipeline_id.serialize_json(
                value["media_live_pipeline_id"]
            )
        )
    if "media_live_channel_output_name" in value:
        out["mediaLiveChannelOutputName"] = value["media_live_channel_output_name"]
    import capo_mediaconnect.types.media_live_transit_encryption

    out["sourceTransitDecryption"] = (
        capo_mediaconnect.types.media_live_transit_encryption.serialize_json(
            value["source_transit_decryption"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaLiveChannelRouterInputConfiguration:
    out: MediaLiveChannelRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if "mediaLiveChannelArn" in data:
        out["media_live_channel_arn"] = data["mediaLiveChannelArn"]
    if "mediaLivePipelineId" in data:
        import capo_mediaconnect.types.media_live_channel_pipeline_id

        out["media_live_pipeline_id"] = (
            capo_mediaconnect.types.media_live_channel_pipeline_id.deserialize_json(
                data["mediaLivePipelineId"]
            )
        )
    if "mediaLiveChannelOutputName" in data:
        out["media_live_channel_output_name"] = data["mediaLiveChannelOutputName"]
    if "sourceTransitDecryption" in data:
        import capo_mediaconnect.types.media_live_transit_encryption

        out["source_transit_decryption"] = (
            capo_mediaconnect.types.media_live_transit_encryption.deserialize_json(
                data["sourceTransitDecryption"]
            )
        )
    else:
        raise DeserializationError(
            "MediaLiveChannelRouterInputConfiguration.source_transit_decryption required"
        )
    return out
