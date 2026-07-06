"""Generated from Smithy shape ``com.amazonaws.medialive#AudioFeedInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class AudioFeedInput(TypedDict, closed=True):
    audio_selector_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the audio selector in the channel that will be sent to the Elemental Inference feed input."""
    feed_input: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the feed input on the Elemental Inference feed that will receive the audio from the specified audio selector."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioFeedInput) -> dict:
    out: dict = {}
    if "audio_selector_name" in value:
        out["audioSelectorName"] = value["audio_selector_name"]
    if "feed_input" in value:
        out["feedInput"] = value["feed_input"]
    return out


def deserialize_json(data: dict) -> AudioFeedInput:
    out: AudioFeedInput = {}  # type: ignore[typeddict-item]
    if "audioSelectorName" in data:
        out["audio_selector_name"] = data["audioSelectorName"]
    if "feedInput" in data:
        out["feed_input"] = data["feedInput"]
    return out
