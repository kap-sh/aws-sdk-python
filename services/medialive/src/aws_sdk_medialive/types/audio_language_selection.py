"""Generated from Smithy shape ``com.amazonaws.medialive#AudioLanguageSelection``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.audio_language_selection_policy


class AudioLanguageSelection(TypedDict):
    language_code: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Selects a specific three-letter language code from within an audio source."""
    language_selection_policy: NotRequired[
        "aws_sdk_medialive.types.audio_language_selection_policy.AudioLanguageSelectionPolicy"
    ]
    r"""When set to \"strict\", the transport stream demux strictly identifies audio streams by their language descriptor. If a PMT update occurs such that an audio stream matching the initially selected language is no longer present then mute will be encoded until the language returns. If \"loose\", then on a PMT update the demux will choose another audio stream in the program with the same stream type if it can't find one with the same language."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioLanguageSelection) -> dict:
    out: dict = {}
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "language_selection_policy" in value:
        import aws_sdk_medialive.types.audio_language_selection_policy

        out["languageSelectionPolicy"] = (
            aws_sdk_medialive.types.audio_language_selection_policy.serialize_json(
                value["language_selection_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioLanguageSelection:
    out: AudioLanguageSelection = {}  # type: ignore[typeddict-item]
    if "languageCode" in data:
        out["language_code"] = data["languageCode"]
    if "languageSelectionPolicy" in data:
        import aws_sdk_medialive.types.audio_language_selection_policy

        out["language_selection_policy"] = (
            aws_sdk_medialive.types.audio_language_selection_policy.deserialize_json(
                data["languageSelectionPolicy"]
            )
        )
    return out
