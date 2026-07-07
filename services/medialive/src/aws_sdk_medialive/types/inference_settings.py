"""Generated from Smithy shape ``com.amazonaws.medialive#InferenceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_audio_feed_input
    import aws_sdk_medialive.types.__string


class InferenceSettings(TypedDict, closed=True):
    feed_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the feed resource that is associated with this channel. The feed is a resource in the Elemental Inference service."""
    audio_feed_inputs: NotRequired[
        "aws_sdk_medialive.types.__list_of_audio_feed_input.__listOfAudioFeedInput"
    ]
    """A list of audio feed inputs that map audio selectors in the channel to feed inputs on the associated Elemental Inference feed."""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceSettings) -> dict:
    out: dict = {}
    if "feed_arn" in value:
        out["feedArn"] = value["feed_arn"]
    if "audio_feed_inputs" in value:
        import aws_sdk_medialive.types.__list_of_audio_feed_input

        out["audioFeedInputs"] = (
            aws_sdk_medialive.types.__list_of_audio_feed_input.serialize_json(
                value["audio_feed_inputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> InferenceSettings:
    out: InferenceSettings = {}  # type: ignore[typeddict-item]
    if "feedArn" in data:
        out["feed_arn"] = data["feedArn"]
    if "audioFeedInputs" in data:
        import aws_sdk_medialive.types.__list_of_audio_feed_input

        out["audio_feed_inputs"] = (
            aws_sdk_medialive.types.__list_of_audio_feed_input.deserialize_json(
                data["audioFeedInputs"]
            )
        )
    return out
