"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsCaptionLanguageMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647
    import aws_sdk_mediaconvert.types.__string
    import aws_sdk_mediaconvert.types.__string_min3_max3_pattern_a_za_z3
    import aws_sdk_mediaconvert.types.language_code


class HlsCaptionLanguageMapping(TypedDict):
    caption_channel: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min_negative2147483648_max2147483647.__integerMinNegative2147483648Max2147483647"
    ]
    """Caption channel."""
    custom_language_code: NotRequired[
        "aws_sdk_mediaconvert.types.__string_min3_max3_pattern_a_za_z3.__stringMin3Max3PatternAZaZ3"
    ]
    """Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code_list.php"""
    language_code: NotRequired["aws_sdk_mediaconvert.types.language_code.LanguageCode"]
    """Specify the language, using an ISO 639-2 three-letter code in all capital letters. You can find a list of codes at: https://www.loc.gov/standards/iso639-2/php/code_list.php"""
    language_description: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """Caption language description."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsCaptionLanguageMapping) -> dict:
    out: dict = {}
    if "caption_channel" in value:
        out["captionChannel"] = value["caption_channel"]
    if "custom_language_code" in value:
        out["customLanguageCode"] = value["custom_language_code"]
    if "language_code" in value:
        import aws_sdk_mediaconvert.types.language_code

        out["languageCode"] = aws_sdk_mediaconvert.types.language_code.serialize_json(
            value["language_code"]
        )
    if "language_description" in value:
        out["languageDescription"] = value["language_description"]
    return out


def deserialize_json(data: dict) -> HlsCaptionLanguageMapping:
    out: HlsCaptionLanguageMapping = {}  # type: ignore[typeddict-item]
    if "captionChannel" in data:
        out["caption_channel"] = data["captionChannel"]
    if "customLanguageCode" in data:
        out["custom_language_code"] = data["customLanguageCode"]
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
