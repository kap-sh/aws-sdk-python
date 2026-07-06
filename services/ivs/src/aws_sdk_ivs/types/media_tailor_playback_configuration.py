"""Generated from Smithy shape ``com.amazonaws.ivs#MediaTailorPlaybackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.media_tailor_playback_configuration_arn


class MediaTailorPlaybackConfiguration(TypedDict, closed=True):
    playback_configuration_arn: NotRequired[
        "aws_sdk_ivs.types.media_tailor_playback_configuration_arn.MediaTailorPlaybackConfigurationArn"
    ]
    """<p>ARN of the customer-created EMT PlaybackConfiguration resource in the same region and account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaTailorPlaybackConfiguration) -> dict:
    out: dict = {}
    if "playback_configuration_arn" in value:
        out["playbackConfigurationArn"] = value["playback_configuration_arn"]
    return out


def deserialize_json(data: dict) -> MediaTailorPlaybackConfiguration:
    out: MediaTailorPlaybackConfiguration = {}  # type: ignore[typeddict-item]
    if "playbackConfigurationArn" in data:
        out["playback_configuration_arn"] = data["playbackConfigurationArn"]
    return out
