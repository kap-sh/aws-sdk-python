"""Generated from Smithy shape ``com.amazonaws.medialive#CmafIngestCaptionLanguageMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1_max4
    import capo_medialive.types.__string_min3_max3


class CmafIngestCaptionLanguageMapping(TypedDict, closed=True):
    caption_channel: NotRequired[
        "capo_medialive.types.__integer_min1_max4.__integerMin1Max4"
    ]
    """A number for the channel for this caption, 1 to 4."""
    language_code: NotRequired[
        "capo_medialive.types.__string_min3_max3.__stringMin3Max3"
    ]
    """Language code for the language of the caption in this channel. For example, ger/deu. See http://www.loc.gov/standards/iso639-2"""


# --- restJson1 ser/de ---
def serialize_json(value: CmafIngestCaptionLanguageMapping) -> dict:
    out: dict = {}
    if "caption_channel" in value:
        out["captionChannel"] = value["caption_channel"]
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    return out


def deserialize_json(data: dict) -> CmafIngestCaptionLanguageMapping:
    out: CmafIngestCaptionLanguageMapping = {}  # type: ignore[typeddict-item]
    if "captionChannel" in data:
        out["caption_channel"] = data["captionChannel"]
    if "languageCode" in data:
        out["language_code"] = data["languageCode"]
    return out
