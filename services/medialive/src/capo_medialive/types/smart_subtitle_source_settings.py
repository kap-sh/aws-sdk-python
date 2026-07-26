"""Generated from Smithy shape ``com.amazonaws.medialive#SmartSubtitleSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.caption_synchronization_mode


class SmartSubtitleSourceSettings(TypedDict, closed=True):
    caption_synchronization_mode: NotRequired[
        "capo_medialive.types.caption_synchronization_mode.CaptionSynchronizationMode"
    ]
    """Controls whether MediaLive delays video to synchronize captions with audio and video output."""
    inference_feed_output: NotRequired["capo_medialive.types.__string.__string"]
    """The name of the Elemental Inference feed output that supplies subtitle input into this caption selector."""


# --- restJson1 ser/de ---
def serialize_json(value: SmartSubtitleSourceSettings) -> dict:
    out: dict = {}
    if "caption_synchronization_mode" in value:
        import capo_medialive.types.caption_synchronization_mode

        out["captionSynchronizationMode"] = (
            capo_medialive.types.caption_synchronization_mode.serialize_json(
                value["caption_synchronization_mode"]
            )
        )
    if "inference_feed_output" in value:
        out["inferenceFeedOutput"] = value["inference_feed_output"]
    return out


def deserialize_json(data: dict) -> SmartSubtitleSourceSettings:
    out: SmartSubtitleSourceSettings = {}  # type: ignore[typeddict-item]
    if "captionSynchronizationMode" in data:
        import capo_medialive.types.caption_synchronization_mode

        out["caption_synchronization_mode"] = (
            capo_medialive.types.caption_synchronization_mode.deserialize_json(
                data["captionSynchronizationMode"]
            )
        )
    if "inferenceFeedOutput" in data:
        out["inference_feed_output"] = data["inferenceFeedOutput"]
    return out
