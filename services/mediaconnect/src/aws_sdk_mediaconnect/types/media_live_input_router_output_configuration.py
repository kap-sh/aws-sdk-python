"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveInputRouterOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_live_input_arn
    import aws_sdk_mediaconnect.types.media_live_input_pipeline_id
    import aws_sdk_mediaconnect.types.media_live_transit_encryption


class MediaLiveInputRouterOutputConfiguration(TypedDict, closed=True):
    media_live_input_arn: NotRequired[
        "aws_sdk_mediaconnect.types.media_live_input_arn.MediaLiveInputArn"
    ]
    """<p>The ARN of the MediaLive input to connect to this router output.</p>"""
    media_live_pipeline_id: NotRequired[
        "aws_sdk_mediaconnect.types.media_live_input_pipeline_id.MediaLiveInputPipelineId"
    ]
    """<p>The index of the MediaLive pipeline to connect to this router output.</p>"""
    destination_transit_encryption: "aws_sdk_mediaconnect.types.media_live_transit_encryption.MediaLiveTransitEncryption"
    """<p>The encryption configuration for the MediaLive input when connected to this router output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveInputRouterOutputConfiguration) -> dict:
    out: dict = {}
    if "media_live_input_arn" in value:
        out["mediaLiveInputArn"] = value["media_live_input_arn"]
    if "media_live_pipeline_id" in value:
        import aws_sdk_mediaconnect.types.media_live_input_pipeline_id

        out["mediaLivePipelineId"] = (
            aws_sdk_mediaconnect.types.media_live_input_pipeline_id.serialize_json(
                value["media_live_pipeline_id"]
            )
        )
    import aws_sdk_mediaconnect.types.media_live_transit_encryption

    out["destinationTransitEncryption"] = (
        aws_sdk_mediaconnect.types.media_live_transit_encryption.serialize_json(
            value["destination_transit_encryption"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaLiveInputRouterOutputConfiguration:
    out: MediaLiveInputRouterOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "mediaLiveInputArn" in data:
        out["media_live_input_arn"] = data["mediaLiveInputArn"]
    if "mediaLivePipelineId" in data:
        import aws_sdk_mediaconnect.types.media_live_input_pipeline_id

        out["media_live_pipeline_id"] = (
            aws_sdk_mediaconnect.types.media_live_input_pipeline_id.deserialize_json(
                data["mediaLivePipelineId"]
            )
        )
    if "destinationTransitEncryption" in data:
        import aws_sdk_mediaconnect.types.media_live_transit_encryption

        out["destination_transit_encryption"] = (
            aws_sdk_mediaconnect.types.media_live_transit_encryption.deserialize_json(
                data["destinationTransitEncryption"]
            )
        )
    else:
        raise DeserializationError(
            "MediaLiveInputRouterOutputConfiguration.destination_transit_encryption required"
        )
    return out
