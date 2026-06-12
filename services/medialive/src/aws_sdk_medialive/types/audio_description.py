"""Generated from Smithy shape ``com.amazonaws.medialive#AudioDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_dash_role_audio
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__string_max255
    import aws_sdk_medialive.types.__string_min1_max35
    import aws_sdk_medialive.types.audio_codec_settings
    import aws_sdk_medialive.types.audio_description_audio_type_control
    import aws_sdk_medialive.types.audio_description_language_code_control
    import aws_sdk_medialive.types.audio_normalization_settings
    import aws_sdk_medialive.types.audio_type
    import aws_sdk_medialive.types.audio_watermark_settings
    import aws_sdk_medialive.types.dvb_dash_accessibility
    import aws_sdk_medialive.types.remix_settings


class AudioDescription(TypedDict):
    audio_normalization_settings: NotRequired[
        "aws_sdk_medialive.types.audio_normalization_settings.AudioNormalizationSettings"
    ]
    """Advanced audio normalization settings."""
    audio_selector_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name of the AudioSelector used as the source for this AudioDescription."""
    audio_type: NotRequired["aws_sdk_medialive.types.audio_type.AudioType"]
    """Applies only if audioTypeControl is useConfigured. The values for audioType are defined in ISO-IEC 13818-1."""
    audio_type_control: NotRequired[
        "aws_sdk_medialive.types.audio_description_audio_type_control.AudioDescriptionAudioTypeControl"
    ]
    """Determines how audio type is determined. followInput: If the input contains an ISO 639 audioType, then that value is passed through to the output. If the input contains no ISO 639 audioType, the value in Audio Type is included in the output. useConfigured: The value in Audio Type is included in the output. Note that this field and audioType are both ignored if inputType is broadcasterMixedAd."""
    audio_watermarking_settings: NotRequired[
        "aws_sdk_medialive.types.audio_watermark_settings.AudioWatermarkSettings"
    ]
    """Settings to configure one or more solutions that insert audio watermarks in the audio encode"""
    codec_settings: NotRequired[
        "aws_sdk_medialive.types.audio_codec_settings.AudioCodecSettings"
    ]
    """Audio codec settings."""
    language_code: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max35.__stringMin1Max35"
    ]
    """RFC 5646 language code representing the language of the audio output track. Only used if languageControlMode is useConfigured, or there is no ISO 639 language code specified in the input."""
    language_code_control: NotRequired[
        "aws_sdk_medialive.types.audio_description_language_code_control.AudioDescriptionLanguageCodeControl"
    ]
    """Choosing followInput will cause the ISO 639 language code of the output to follow the ISO 639 language code of the input. The languageCode will be used when useConfigured is set, or when followInput is selected but there is no ISO 639 language code specified by the input."""
    name: NotRequired["aws_sdk_medialive.types.__string_max255.__stringMax255"]
    """The name of this AudioDescription. Outputs will use this name to uniquely identify this AudioDescription. Description names should be unique within this Live Event."""
    remix_settings: NotRequired["aws_sdk_medialive.types.remix_settings.RemixSettings"]
    """Settings that control how input audio channels are remixed into the output audio channels."""
    stream_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Used for MS Smooth and Apple HLS outputs. Indicates the name displayed by the player (eg. English, or Director Commentary)."""
    audio_dash_roles: NotRequired[
        "aws_sdk_medialive.types.__list_of_dash_role_audio.__listOfDashRoleAudio"
    ]
    """Identifies the DASH roles to assign to this audio output. Applies only when the audio output is configured for DVB DASH accessibility signaling."""
    dvb_dash_accessibility: NotRequired[
        "aws_sdk_medialive.types.dvb_dash_accessibility.DvbDashAccessibility"
    ]
    """Identifies DVB DASH accessibility signaling in this audio output. Used in Microsoft Smooth Streaming outputs to signal accessibility information to packagers."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioDescription) -> dict:
    out: dict = {}
    if "audio_normalization_settings" in value:
        import aws_sdk_medialive.types.audio_normalization_settings

        out["audioNormalizationSettings"] = (
            aws_sdk_medialive.types.audio_normalization_settings.serialize_json(
                value["audio_normalization_settings"]
            )
        )
    if "audio_selector_name" in value:
        out["audioSelectorName"] = value["audio_selector_name"]
    if "audio_type" in value:
        import aws_sdk_medialive.types.audio_type

        out["audioType"] = aws_sdk_medialive.types.audio_type.serialize_json(
            value["audio_type"]
        )
    if "audio_type_control" in value:
        import aws_sdk_medialive.types.audio_description_audio_type_control

        out["audioTypeControl"] = (
            aws_sdk_medialive.types.audio_description_audio_type_control.serialize_json(
                value["audio_type_control"]
            )
        )
    if "audio_watermarking_settings" in value:
        import aws_sdk_medialive.types.audio_watermark_settings

        out["audioWatermarkingSettings"] = (
            aws_sdk_medialive.types.audio_watermark_settings.serialize_json(
                value["audio_watermarking_settings"]
            )
        )
    if "codec_settings" in value:
        import aws_sdk_medialive.types.audio_codec_settings

        out["codecSettings"] = (
            aws_sdk_medialive.types.audio_codec_settings.serialize_json(
                value["codec_settings"]
            )
        )
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "language_code_control" in value:
        import aws_sdk_medialive.types.audio_description_language_code_control

        out["languageCodeControl"] = (
            aws_sdk_medialive.types.audio_description_language_code_control.serialize_json(
                value["language_code_control"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "remix_settings" in value:
        import aws_sdk_medialive.types.remix_settings

        out["remixSettings"] = aws_sdk_medialive.types.remix_settings.serialize_json(
            value["remix_settings"]
        )
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    if "audio_dash_roles" in value:
        import aws_sdk_medialive.types.__list_of_dash_role_audio

        out["audioDashRoles"] = (
            aws_sdk_medialive.types.__list_of_dash_role_audio.serialize_json(
                value["audio_dash_roles"]
            )
        )
    if "dvb_dash_accessibility" in value:
        import aws_sdk_medialive.types.dvb_dash_accessibility

        out["dvbDashAccessibility"] = (
            aws_sdk_medialive.types.dvb_dash_accessibility.serialize_json(
                value["dvb_dash_accessibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioDescription:
    out: AudioDescription = {}  # type: ignore[typeddict-item]
    if "audioNormalizationSettings" in data:
        import aws_sdk_medialive.types.audio_normalization_settings

        out["audio_normalization_settings"] = (
            aws_sdk_medialive.types.audio_normalization_settings.deserialize_json(
                data["audioNormalizationSettings"]
            )
        )
    if "audioSelectorName" in data:
        out["audio_selector_name"] = data["audioSelectorName"]
    if "audioType" in data:
        import aws_sdk_medialive.types.audio_type

        out["audio_type"] = aws_sdk_medialive.types.audio_type.deserialize_json(
            data["audioType"]
        )
    if "audioTypeControl" in data:
        import aws_sdk_medialive.types.audio_description_audio_type_control

        out["audio_type_control"] = (
            aws_sdk_medialive.types.audio_description_audio_type_control.deserialize_json(
                data["audioTypeControl"]
            )
        )
    if "audioWatermarkingSettings" in data:
        import aws_sdk_medialive.types.audio_watermark_settings

        out["audio_watermarking_settings"] = (
            aws_sdk_medialive.types.audio_watermark_settings.deserialize_json(
                data["audioWatermarkingSettings"]
            )
        )
    if "codecSettings" in data:
        import aws_sdk_medialive.types.audio_codec_settings

        out["codec_settings"] = (
            aws_sdk_medialive.types.audio_codec_settings.deserialize_json(
                data["codecSettings"]
            )
        )
    if "languageCode" in data:
        out["language_code"] = data["languageCode"]
    if "languageCodeControl" in data:
        import aws_sdk_medialive.types.audio_description_language_code_control

        out["language_code_control"] = (
            aws_sdk_medialive.types.audio_description_language_code_control.deserialize_json(
                data["languageCodeControl"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "remixSettings" in data:
        import aws_sdk_medialive.types.remix_settings

        out["remix_settings"] = aws_sdk_medialive.types.remix_settings.deserialize_json(
            data["remixSettings"]
        )
    if "streamName" in data:
        out["stream_name"] = data["streamName"]
    if "audioDashRoles" in data:
        import aws_sdk_medialive.types.__list_of_dash_role_audio

        out["audio_dash_roles"] = (
            aws_sdk_medialive.types.__list_of_dash_role_audio.deserialize_json(
                data["audioDashRoles"]
            )
        )
    if "dvbDashAccessibility" in data:
        import aws_sdk_medialive.types.dvb_dash_accessibility

        out["dvb_dash_accessibility"] = (
            aws_sdk_medialive.types.dvb_dash_accessibility.deserialize_json(
                data["dvbDashAccessibility"]
            )
        )
    return out
