"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PresetSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_audio_description
    import capo_mediaconvert.types.__list_of_caption_description_preset
    import capo_mediaconvert.types.container_settings
    import capo_mediaconvert.types.video_description


class PresetSettings(TypedDict, closed=True):
    audio_descriptions: NotRequired[
        "capo_mediaconvert.types.__list_of_audio_description.__listOfAudioDescription"
    ]
    """Contains groups of audio encoding settings organized by audio codec. Include one instance of per output. Can contain multiple groups of encoding settings."""
    caption_descriptions: NotRequired[
        "capo_mediaconvert.types.__list_of_caption_description_preset.__listOfCaptionDescriptionPreset"
    ]
    """This object holds groups of settings related to captions for one output. For each output that has captions, include one instance of CaptionDescriptions."""
    container_settings: NotRequired[
        "capo_mediaconvert.types.container_settings.ContainerSettings"
    ]
    """Container specific settings."""
    video_description: NotRequired[
        "capo_mediaconvert.types.video_description.VideoDescription"
    ]
    """VideoDescription contains a group of video encoding settings. The specific video settings depend on the video codec that you choose for the property codec. Include one instance of VideoDescription per output."""


# --- restJson1 ser/de ---
def serialize_json(value: PresetSettings) -> dict:
    out: dict = {}
    if "audio_descriptions" in value:
        import capo_mediaconvert.types.__list_of_audio_description

        out["audioDescriptions"] = (
            capo_mediaconvert.types.__list_of_audio_description.serialize_json(
                value["audio_descriptions"]
            )
        )
    if "caption_descriptions" in value:
        import capo_mediaconvert.types.__list_of_caption_description_preset

        out["captionDescriptions"] = (
            capo_mediaconvert.types.__list_of_caption_description_preset.serialize_json(
                value["caption_descriptions"]
            )
        )
    if "container_settings" in value:
        import capo_mediaconvert.types.container_settings

        out["containerSettings"] = (
            capo_mediaconvert.types.container_settings.serialize_json(
                value["container_settings"]
            )
        )
    if "video_description" in value:
        import capo_mediaconvert.types.video_description

        out["videoDescription"] = (
            capo_mediaconvert.types.video_description.serialize_json(
                value["video_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> PresetSettings:
    out: PresetSettings = {}  # type: ignore[typeddict-item]
    if "audioDescriptions" in data:
        import capo_mediaconvert.types.__list_of_audio_description

        out["audio_descriptions"] = (
            capo_mediaconvert.types.__list_of_audio_description.deserialize_json(
                data["audioDescriptions"]
            )
        )
    if "captionDescriptions" in data:
        import capo_mediaconvert.types.__list_of_caption_description_preset

        out["caption_descriptions"] = (
            capo_mediaconvert.types.__list_of_caption_description_preset.deserialize_json(
                data["captionDescriptions"]
            )
        )
    if "containerSettings" in data:
        import capo_mediaconvert.types.container_settings

        out["container_settings"] = (
            capo_mediaconvert.types.container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    if "videoDescription" in data:
        import capo_mediaconvert.types.video_description

        out["video_description"] = (
            capo_mediaconvert.types.video_description.deserialize_json(
                data["videoDescription"]
            )
        )
    return out
