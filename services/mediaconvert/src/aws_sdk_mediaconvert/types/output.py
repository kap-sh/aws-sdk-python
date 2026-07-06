"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Output``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of_audio_description
    import aws_sdk_mediaconvert.types.__list_of_caption_description
    import aws_sdk_mediaconvert.types.__string_max256
    import aws_sdk_mediaconvert.types.__string_min0
    import aws_sdk_mediaconvert.types.__string_min1_max256
    import aws_sdk_mediaconvert.types.container_settings
    import aws_sdk_mediaconvert.types.output_settings
    import aws_sdk_mediaconvert.types.video_description


class Output(TypedDict, closed=True):
    audio_descriptions: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_audio_description.__listOfAudioDescription"
    ]
    """Contains groups of audio encoding settings organized by audio codec. Include one instance of per output. Can contain multiple groups of encoding settings."""
    caption_descriptions: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of_caption_description.__listOfCaptionDescription"
    ]
    """Contains groups of captions settings. For each output that has captions, include one instance of CaptionDescriptions. Can contain multiple groups of captions settings."""
    container_settings: NotRequired[
        "aws_sdk_mediaconvert.types.container_settings.ContainerSettings"
    ]
    """Container specific settings."""
    extension: NotRequired["aws_sdk_mediaconvert.types.__string_max256.__stringMax256"]
    """Use Extension to specify the file extension for outputs in File output groups. If you do not specify a value, the service will use default extensions by container type as follows * MPEG-2 transport stream, m2ts * Quicktime, mov * MXF container, mxf * MPEG-4 container, mp4 * WebM container, webm * Animated GIF container, gif * No Container, the service will use codec extensions (e.g. AAC, H265, H265, AC3)"""
    name_modifier: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min1_max256.__stringMin1Max256"
    ]
    """Use Name modifier to have the service add a string to the end of each output filename. You specify the base filename as part of your destination URI. When you create multiple outputs in the same output group, Name modifier is required. Name modifier also accepts format identifiers. For DASH ISO outputs, if you use the format identifiers $Number$ or $Time$ in one output, you must use them in the same way in all outputs of the output group."""
    output_settings: NotRequired[
        "aws_sdk_mediaconvert.types.output_settings.OutputSettings"
    ]
    """Specific settings for this type of output."""
    preset: NotRequired["aws_sdk_mediaconvert.types.__string_min0.__stringMin0"]
    """Use Preset to specify a preset for your transcoding settings. Provide the system or custom preset name. You can specify either Preset or Container settings, but not both."""
    video_description: NotRequired[
        "aws_sdk_mediaconvert.types.video_description.VideoDescription"
    ]
    """VideoDescription contains a group of video encoding settings. The specific video settings depend on the video codec that you choose for the property codec. Include one instance of VideoDescription per output."""


# --- restJson1 ser/de ---
def serialize_json(value: Output) -> dict:
    out: dict = {}
    if "audio_descriptions" in value:
        import aws_sdk_mediaconvert.types.__list_of_audio_description

        out["audioDescriptions"] = (
            aws_sdk_mediaconvert.types.__list_of_audio_description.serialize_json(
                value["audio_descriptions"]
            )
        )
    if "caption_descriptions" in value:
        import aws_sdk_mediaconvert.types.__list_of_caption_description

        out["captionDescriptions"] = (
            aws_sdk_mediaconvert.types.__list_of_caption_description.serialize_json(
                value["caption_descriptions"]
            )
        )
    if "container_settings" in value:
        import aws_sdk_mediaconvert.types.container_settings

        out["containerSettings"] = (
            aws_sdk_mediaconvert.types.container_settings.serialize_json(
                value["container_settings"]
            )
        )
    if "extension" in value:
        out["extension"] = value["extension"]
    if "name_modifier" in value:
        out["nameModifier"] = value["name_modifier"]
    if "output_settings" in value:
        import aws_sdk_mediaconvert.types.output_settings

        out["outputSettings"] = (
            aws_sdk_mediaconvert.types.output_settings.serialize_json(
                value["output_settings"]
            )
        )
    if "preset" in value:
        out["preset"] = value["preset"]
    if "video_description" in value:
        import aws_sdk_mediaconvert.types.video_description

        out["videoDescription"] = (
            aws_sdk_mediaconvert.types.video_description.serialize_json(
                value["video_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> Output:
    out: Output = {}  # type: ignore[typeddict-item]
    if "audioDescriptions" in data:
        import aws_sdk_mediaconvert.types.__list_of_audio_description

        out["audio_descriptions"] = (
            aws_sdk_mediaconvert.types.__list_of_audio_description.deserialize_json(
                data["audioDescriptions"]
            )
        )
    if "captionDescriptions" in data:
        import aws_sdk_mediaconvert.types.__list_of_caption_description

        out["caption_descriptions"] = (
            aws_sdk_mediaconvert.types.__list_of_caption_description.deserialize_json(
                data["captionDescriptions"]
            )
        )
    if "containerSettings" in data:
        import aws_sdk_mediaconvert.types.container_settings

        out["container_settings"] = (
            aws_sdk_mediaconvert.types.container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    if "extension" in data:
        out["extension"] = data["extension"]
    if "nameModifier" in data:
        out["name_modifier"] = data["nameModifier"]
    if "outputSettings" in data:
        import aws_sdk_mediaconvert.types.output_settings

        out["output_settings"] = (
            aws_sdk_mediaconvert.types.output_settings.deserialize_json(
                data["outputSettings"]
            )
        )
    if "preset" in data:
        out["preset"] = data["preset"]
    if "videoDescription" in data:
        import aws_sdk_mediaconvert.types.video_description

        out["video_description"] = (
            aws_sdk_mediaconvert.types.video_description.deserialize_json(
                data["videoDescription"]
            )
        )
    return out
