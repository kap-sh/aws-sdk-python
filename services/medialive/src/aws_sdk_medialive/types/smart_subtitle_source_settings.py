"""Generated from Smithy shape ``com.amazonaws.medialive#SmartSubtitleSourceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.caption_synchronization_mode


class SmartSubtitleSourceSettings(TypedDict):
    caption_synchronization_mode: NotRequired[
        "aws_sdk_medialive.types.caption_synchronization_mode.CaptionSynchronizationMode"
    ]
    """Controls whether MediaLive delays video to synchronize captions with audio and video output."""
    inference_feed_output: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the Elemental Inference feed output that supplies subtitle input into this caption selector."""


# --- restJson1 ser/de ---
def serialize_json(value: SmartSubtitleSourceSettings) -> dict:
    out: dict = {}
    if "caption_synchronization_mode" in value:
        import aws_sdk_medialive.types.caption_synchronization_mode

        out["captionSynchronizationMode"] = (
            aws_sdk_medialive.types.caption_synchronization_mode.serialize_json(
                value["caption_synchronization_mode"]
            )
        )
    if "inference_feed_output" in value:
        out["inferenceFeedOutput"] = value["inference_feed_output"]
    return out


def deserialize_json(data: dict) -> SmartSubtitleSourceSettings:
    out: SmartSubtitleSourceSettings = {}  # type: ignore[typeddict-item]
    if "captionSynchronizationMode" in data:
        import aws_sdk_medialive.types.caption_synchronization_mode

        out["caption_synchronization_mode"] = (
            aws_sdk_medialive.types.caption_synchronization_mode.deserialize_json(
                data["captionSynchronizationMode"]
            )
        )
    if "inferenceFeedOutput" in data:
        out["inference_feed_output"] = data["inferenceFeedOutput"]
    return out
