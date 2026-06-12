"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionDescriptionPreset``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__string_pattern_a_za_z23_a_za_z
    import aws_sdk_mediaconvert.types.caption_destination_settings
    import aws_sdk_mediaconvert.types.language_code


class CaptionDescriptionPreset(TypedDict):
    custom_language_code: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_a_za_z23_a_za_z.__stringPatternAZaZ23AZaZ"
    ]
    """Specify the language for this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information when automatically selecting the font script for rendering the captions text. For all outputs, you can use an ISO 639-2 or ISO 639-3 code. For streaming outputs, you can also use any other code in the full RFC-5646 specification. Streaming outputs are those that are in one of the following output groups: CMAF, DASH ISO, Apple HLS, or Microsoft Smooth Streaming."""
    destination_settings: NotRequired[
        "aws_sdk_mediaconvert.types.caption_destination_settings.CaptionDestinationSettings"
    ]
    """Settings related to one captions tab on the MediaConvert console. Usually, one captions tab corresponds to one output captions track. Depending on your output captions format, one tab might correspond to a set of output captions tracks. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/including-captions.html."""
    language_code: NotRequired["aws_sdk_mediaconvert.types.language_code.LanguageCode"]
    """Specify the language of this captions output track. For most captions output formats, the encoder puts this language information in the output captions metadata. If your output captions format is DVB-Sub or Burn in, the encoder uses this language information to choose the font language for rendering the captions text."""
    language_description: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Specify a label for this set of output captions. For example, \"English\", \"Director commentary\", or \"track_2\". For streaming outputs, MediaConvert passes this information into destination manifests for display on the end-viewer's player device. For outputs in other output groups, the service ignores this setting."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionDescriptionPreset) -> dict:
    out: dict = {}
    if "custom_language_code" in value:
        out["customLanguageCode"] = value["custom_language_code"]
    if "destination_settings" in value:
        import aws_sdk_mediaconvert.types.caption_destination_settings

        out["destinationSettings"] = (
            aws_sdk_mediaconvert.types.caption_destination_settings.serialize_json(
                value["destination_settings"]
            )
        )
    if "language_code" in value:
        import aws_sdk_mediaconvert.types.language_code

        out["languageCode"] = aws_sdk_mediaconvert.types.language_code.serialize_json(
            value["language_code"]
        )
    if "language_description" in value:
        out["languageDescription"] = value["language_description"]
    return out


def deserialize_json(data: dict) -> CaptionDescriptionPreset:
    out: CaptionDescriptionPreset = {}  # type: ignore[typeddict-item]
    if "customLanguageCode" in data:
        out["custom_language_code"] = data["customLanguageCode"]
    if "destinationSettings" in data:
        import aws_sdk_mediaconvert.types.caption_destination_settings

        out["destination_settings"] = (
            aws_sdk_mediaconvert.types.caption_destination_settings.deserialize_json(
                data["destinationSettings"]
            )
        )
    if "languageCode" in data:
        import aws_sdk_mediaconvert.types.language_code

        out["language_code"] = (
            aws_sdk_mediaconvert.types.language_code.deserialize_json(
                data["languageCode"]
            )
        )
    if "languageDescription" in data:
        out["language_description"] = data["languageDescription"]
    return out
