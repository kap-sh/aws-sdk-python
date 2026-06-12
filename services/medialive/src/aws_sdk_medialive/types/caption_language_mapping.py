"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionLanguageMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1_max4
    import aws_sdk_medialive.types.__string_min1
    import aws_sdk_medialive.types.__string_min3_max3


class CaptionLanguageMapping(TypedDict):
    caption_channel: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max4.__integerMin1Max4"
    ]
    """The closed caption channel being described by this CaptionLanguageMapping. Each channel mapping must have a unique channel number (maximum of 4)"""
    language_code: NotRequired[
        "aws_sdk_medialive.types.__string_min3_max3.__stringMin3Max3"
    ]
    """Three character ISO 639-2 language code (see http://www.loc.gov/standards/iso639-2)"""
    language_description: NotRequired[
        "aws_sdk_medialive.types.__string_min1.__stringMin1"
    ]
    """Textual description of language"""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionLanguageMapping) -> dict:
    out: dict = {}
    if "caption_channel" in value:
        out["captionChannel"] = value["caption_channel"]
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "language_description" in value:
        out["languageDescription"] = value["language_description"]
    return out


def deserialize_json(data: dict) -> CaptionLanguageMapping:
    out: CaptionLanguageMapping = {}  # type: ignore[typeddict-item]
    if "captionChannel" in data:
        out["caption_channel"] = data["captionChannel"]
    if "languageCode" in data:
        out["language_code"] = data["languageCode"]
    if "languageDescription" in data:
        out["language_description"] = data["languageDescription"]
    return out
