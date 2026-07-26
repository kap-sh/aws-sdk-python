"""Generated from Smithy shape ``com.amazonaws.connectparticipant#MeetingFeaturesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.audio_features


class MeetingFeaturesConfiguration(TypedDict, closed=True):
    audio: NotRequired["capo_connectparticipant.types.audio_features.AudioFeatures"]
    """<p>The configuration settings for the audio features available to a meeting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MeetingFeaturesConfiguration) -> dict:
    out: dict = {}
    if "audio" in value:
        import capo_connectparticipant.types.audio_features

        out["Audio"] = capo_connectparticipant.types.audio_features.serialize_json(
            value["audio"]
        )
    return out


def deserialize_json(data: dict) -> MeetingFeaturesConfiguration:
    out: MeetingFeaturesConfiguration = {}  # type: ignore[typeddict-item]
    if "Audio" in data:
        import capo_connectparticipant.types.audio_features

        out["audio"] = capo_connectparticipant.types.audio_features.deserialize_json(
            data["Audio"]
        )
    return out
