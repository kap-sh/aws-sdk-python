"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DynamicAudioSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647
    import aws_sdk_mediaconvert.types.__string_pattern_s3_https
    import aws_sdk_mediaconvert.types.audio_duration_correction
    import aws_sdk_mediaconvert.types.dynamic_audio_selector_type
    import aws_sdk_mediaconvert.types.language_code


class DynamicAudioSelector(TypedDict, closed=True):
    audio_duration_correction: NotRequired[
        "aws_sdk_mediaconvert.types.audio_duration_correction.AudioDurationCorrection"
    ]
    """Apply audio timing corrections to help synchronize audio and video in your output. To apply timing corrections, your input must meet the following requirements: * Container: MP4, or MOV, with an accurate time-to-sample (STTS) table. * Audio track: AAC. Choose from the following audio timing correction settings: * Disabled (Default): Apply no correction. * Auto: Recommended for most inputs. MediaConvert analyzes the audio timing in your input and determines which correction setting to use, if needed. * Track: Adjust the duration of each audio frame by a constant amount to align the audio track length with STTS duration. Track-level correction does not affect pitch, and is recommended for tonal audio content such as music. * Frame: Adjust the duration of each audio frame by a variable amount to align audio frames with STTS timestamps. No corrections are made to already-aligned frames. Frame-level correction may affect the pitch of corrected frames, and is recommended for atonal audio content such as speech or percussion. * Force: Apply audio duration correction, either Track or Frame depending on your input, regardless of the accuracy of your input's STTS table. Your output audio and video may not be aligned or it may contain audio artifacts."""
    external_audio_file_input: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_s3_https.__stringPatternS3Https"
    ]
    """Specify the S3, HTTP, or HTTPS URL for your external audio file input."""
    language_code: NotRequired["aws_sdk_mediaconvert.types.language_code.LanguageCode"]
    """Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code_list.php"""
    offset: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Specify a time delta, in milliseconds, to offset the audio from the input video. To specify no offset: Keep the default value, 0. To specify an offset: Enter an integer from -2147483648 to 2147483647"""
    selector_type: NotRequired[
        "aws_sdk_mediaconvert.types.dynamic_audio_selector_type.DynamicAudioSelectorType"
    ]
    """Specify which audio tracks to dynamically select from your source. To select all audio tracks: Keep the default value, All tracks. To select all audio tracks with a specific language code: Choose Language code. When you do, you must also specify a language code under the Language code setting. If there is no matching Language code in your source, then no track will be selected."""


# --- restJson1 ser/de ---
def serialize_json(value: DynamicAudioSelector) -> dict:
    out: dict = {}
    if "audio_duration_correction" in value:
        import aws_sdk_mediaconvert.types.audio_duration_correction

        out["audioDurationCorrection"] = (
            aws_sdk_mediaconvert.types.audio_duration_correction.serialize_json(
                value["audio_duration_correction"]
            )
        )
    if "external_audio_file_input" in value:
        out["externalAudioFileInput"] = value["external_audio_file_input"]
    if "language_code" in value:
        import aws_sdk_mediaconvert.types.language_code

        out["languageCode"] = aws_sdk_mediaconvert.types.language_code.serialize_json(
            value["language_code"]
        )
    if "offset" in value:
        out["offset"] = value["offset"]
    if "selector_type" in value:
        import aws_sdk_mediaconvert.types.dynamic_audio_selector_type

        out["selectorType"] = (
            aws_sdk_mediaconvert.types.dynamic_audio_selector_type.serialize_json(
                value["selector_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DynamicAudioSelector:
    out: DynamicAudioSelector = {}  # type: ignore[typeddict-item]
    if "audioDurationCorrection" in data:
        import aws_sdk_mediaconvert.types.audio_duration_correction

        out["audio_duration_correction"] = (
            aws_sdk_mediaconvert.types.audio_duration_correction.deserialize_json(
                data["audioDurationCorrection"]
            )
        )
    if "externalAudioFileInput" in data:
        out["external_audio_file_input"] = data["externalAudioFileInput"]
    if "languageCode" in data:
        import aws_sdk_mediaconvert.types.language_code

        out["language_code"] = (
            aws_sdk_mediaconvert.types.language_code.deserialize_json(
                data["languageCode"]
            )
        )
    if "offset" in data:
        out["offset"] = data["offset"]
    if "selectorType" in data:
        import aws_sdk_mediaconvert.types.dynamic_audio_selector_type

        out["selector_type"] = (
            aws_sdk_mediaconvert.types.dynamic_audio_selector_type.deserialize_json(
                data["selectorType"]
            )
        )
    return out
