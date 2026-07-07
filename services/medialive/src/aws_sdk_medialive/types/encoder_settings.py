"""Generated from Smithy shape ``com.amazonaws.medialive#EncoderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_audio_description
    import aws_sdk_medialive.types.__list_of_caption_description
    import aws_sdk_medialive.types.__list_of_output_group
    import aws_sdk_medialive.types.__list_of_video_description
    import aws_sdk_medialive.types.avail_blanking
    import aws_sdk_medialive.types.avail_configuration
    import aws_sdk_medialive.types.blackout_slate
    import aws_sdk_medialive.types.color_correction_settings
    import aws_sdk_medialive.types.feature_activations
    import aws_sdk_medialive.types.global_configuration
    import aws_sdk_medialive.types.motion_graphics_configuration
    import aws_sdk_medialive.types.nielsen_configuration
    import aws_sdk_medialive.types.thumbnail_configuration
    import aws_sdk_medialive.types.timecode_config


class EncoderSettings(TypedDict, closed=True):
    audio_descriptions: NotRequired[
        "aws_sdk_medialive.types.__list_of_audio_description.__listOfAudioDescription"
    ]
    avail_blanking: NotRequired["aws_sdk_medialive.types.avail_blanking.AvailBlanking"]
    """Settings for ad avail blanking."""
    avail_configuration: NotRequired[
        "aws_sdk_medialive.types.avail_configuration.AvailConfiguration"
    ]
    """Event-wide configuration settings for ad avail insertion."""
    blackout_slate: NotRequired["aws_sdk_medialive.types.blackout_slate.BlackoutSlate"]
    """Settings for blackout slate."""
    caption_descriptions: NotRequired[
        "aws_sdk_medialive.types.__list_of_caption_description.__listOfCaptionDescription"
    ]
    """Settings for caption decriptions"""
    feature_activations: NotRequired[
        "aws_sdk_medialive.types.feature_activations.FeatureActivations"
    ]
    """Feature Activations"""
    global_configuration: NotRequired[
        "aws_sdk_medialive.types.global_configuration.GlobalConfiguration"
    ]
    """Configuration settings that apply to the event as a whole."""
    motion_graphics_configuration: NotRequired[
        "aws_sdk_medialive.types.motion_graphics_configuration.MotionGraphicsConfiguration"
    ]
    """Settings for motion graphics."""
    nielsen_configuration: NotRequired[
        "aws_sdk_medialive.types.nielsen_configuration.NielsenConfiguration"
    ]
    """Nielsen configuration settings."""
    output_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of_output_group.__listOfOutputGroup"
    ]
    timecode_config: NotRequired[
        "aws_sdk_medialive.types.timecode_config.TimecodeConfig"
    ]
    """Contains settings used to acquire and adjust timecode information from inputs."""
    video_descriptions: NotRequired[
        "aws_sdk_medialive.types.__list_of_video_description.__listOfVideoDescription"
    ]
    thumbnail_configuration: NotRequired[
        "aws_sdk_medialive.types.thumbnail_configuration.ThumbnailConfiguration"
    ]
    """Thumbnail configuration settings."""
    color_correction_settings: NotRequired[
        "aws_sdk_medialive.types.color_correction_settings.ColorCorrectionSettings"
    ]
    """Color Correction Settings"""


# --- restJson1 ser/de ---
def serialize_json(value: EncoderSettings) -> dict:
    out: dict = {}
    if "audio_descriptions" in value:
        import aws_sdk_medialive.types.__list_of_audio_description

        out["audioDescriptions"] = (
            aws_sdk_medialive.types.__list_of_audio_description.serialize_json(
                value["audio_descriptions"]
            )
        )
    if "avail_blanking" in value:
        import aws_sdk_medialive.types.avail_blanking

        out["availBlanking"] = aws_sdk_medialive.types.avail_blanking.serialize_json(
            value["avail_blanking"]
        )
    if "avail_configuration" in value:
        import aws_sdk_medialive.types.avail_configuration

        out["availConfiguration"] = (
            aws_sdk_medialive.types.avail_configuration.serialize_json(
                value["avail_configuration"]
            )
        )
    if "blackout_slate" in value:
        import aws_sdk_medialive.types.blackout_slate

        out["blackoutSlate"] = aws_sdk_medialive.types.blackout_slate.serialize_json(
            value["blackout_slate"]
        )
    if "caption_descriptions" in value:
        import aws_sdk_medialive.types.__list_of_caption_description

        out["captionDescriptions"] = (
            aws_sdk_medialive.types.__list_of_caption_description.serialize_json(
                value["caption_descriptions"]
            )
        )
    if "feature_activations" in value:
        import aws_sdk_medialive.types.feature_activations

        out["featureActivations"] = (
            aws_sdk_medialive.types.feature_activations.serialize_json(
                value["feature_activations"]
            )
        )
    if "global_configuration" in value:
        import aws_sdk_medialive.types.global_configuration

        out["globalConfiguration"] = (
            aws_sdk_medialive.types.global_configuration.serialize_json(
                value["global_configuration"]
            )
        )
    if "motion_graphics_configuration" in value:
        import aws_sdk_medialive.types.motion_graphics_configuration

        out["motionGraphicsConfiguration"] = (
            aws_sdk_medialive.types.motion_graphics_configuration.serialize_json(
                value["motion_graphics_configuration"]
            )
        )
    if "nielsen_configuration" in value:
        import aws_sdk_medialive.types.nielsen_configuration

        out["nielsenConfiguration"] = (
            aws_sdk_medialive.types.nielsen_configuration.serialize_json(
                value["nielsen_configuration"]
            )
        )
    if "output_groups" in value:
        import aws_sdk_medialive.types.__list_of_output_group

        out["outputGroups"] = (
            aws_sdk_medialive.types.__list_of_output_group.serialize_json(
                value["output_groups"]
            )
        )
    if "timecode_config" in value:
        import aws_sdk_medialive.types.timecode_config

        out["timecodeConfig"] = aws_sdk_medialive.types.timecode_config.serialize_json(
            value["timecode_config"]
        )
    if "video_descriptions" in value:
        import aws_sdk_medialive.types.__list_of_video_description

        out["videoDescriptions"] = (
            aws_sdk_medialive.types.__list_of_video_description.serialize_json(
                value["video_descriptions"]
            )
        )
    if "thumbnail_configuration" in value:
        import aws_sdk_medialive.types.thumbnail_configuration

        out["thumbnailConfiguration"] = (
            aws_sdk_medialive.types.thumbnail_configuration.serialize_json(
                value["thumbnail_configuration"]
            )
        )
    if "color_correction_settings" in value:
        import aws_sdk_medialive.types.color_correction_settings

        out["colorCorrectionSettings"] = (
            aws_sdk_medialive.types.color_correction_settings.serialize_json(
                value["color_correction_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncoderSettings:
    out: EncoderSettings = {}  # type: ignore[typeddict-item]
    if "audioDescriptions" in data:
        import aws_sdk_medialive.types.__list_of_audio_description

        out["audio_descriptions"] = (
            aws_sdk_medialive.types.__list_of_audio_description.deserialize_json(
                data["audioDescriptions"]
            )
        )
    if "availBlanking" in data:
        import aws_sdk_medialive.types.avail_blanking

        out["avail_blanking"] = aws_sdk_medialive.types.avail_blanking.deserialize_json(
            data["availBlanking"]
        )
    if "availConfiguration" in data:
        import aws_sdk_medialive.types.avail_configuration

        out["avail_configuration"] = (
            aws_sdk_medialive.types.avail_configuration.deserialize_json(
                data["availConfiguration"]
            )
        )
    if "blackoutSlate" in data:
        import aws_sdk_medialive.types.blackout_slate

        out["blackout_slate"] = aws_sdk_medialive.types.blackout_slate.deserialize_json(
            data["blackoutSlate"]
        )
    if "captionDescriptions" in data:
        import aws_sdk_medialive.types.__list_of_caption_description

        out["caption_descriptions"] = (
            aws_sdk_medialive.types.__list_of_caption_description.deserialize_json(
                data["captionDescriptions"]
            )
        )
    if "featureActivations" in data:
        import aws_sdk_medialive.types.feature_activations

        out["feature_activations"] = (
            aws_sdk_medialive.types.feature_activations.deserialize_json(
                data["featureActivations"]
            )
        )
    if "globalConfiguration" in data:
        import aws_sdk_medialive.types.global_configuration

        out["global_configuration"] = (
            aws_sdk_medialive.types.global_configuration.deserialize_json(
                data["globalConfiguration"]
            )
        )
    if "motionGraphicsConfiguration" in data:
        import aws_sdk_medialive.types.motion_graphics_configuration

        out["motion_graphics_configuration"] = (
            aws_sdk_medialive.types.motion_graphics_configuration.deserialize_json(
                data["motionGraphicsConfiguration"]
            )
        )
    if "nielsenConfiguration" in data:
        import aws_sdk_medialive.types.nielsen_configuration

        out["nielsen_configuration"] = (
            aws_sdk_medialive.types.nielsen_configuration.deserialize_json(
                data["nielsenConfiguration"]
            )
        )
    if "outputGroups" in data:
        import aws_sdk_medialive.types.__list_of_output_group

        out["output_groups"] = (
            aws_sdk_medialive.types.__list_of_output_group.deserialize_json(
                data["outputGroups"]
            )
        )
    if "timecodeConfig" in data:
        import aws_sdk_medialive.types.timecode_config

        out["timecode_config"] = (
            aws_sdk_medialive.types.timecode_config.deserialize_json(
                data["timecodeConfig"]
            )
        )
    if "videoDescriptions" in data:
        import aws_sdk_medialive.types.__list_of_video_description

        out["video_descriptions"] = (
            aws_sdk_medialive.types.__list_of_video_description.deserialize_json(
                data["videoDescriptions"]
            )
        )
    if "thumbnailConfiguration" in data:
        import aws_sdk_medialive.types.thumbnail_configuration

        out["thumbnail_configuration"] = (
            aws_sdk_medialive.types.thumbnail_configuration.deserialize_json(
                data["thumbnailConfiguration"]
            )
        )
    if "colorCorrectionSettings" in data:
        import aws_sdk_medialive.types.color_correction_settings

        out["color_correction_settings"] = (
            aws_sdk_medialive.types.color_correction_settings.deserialize_json(
                data["colorCorrectionSettings"]
            )
        )
    return out
