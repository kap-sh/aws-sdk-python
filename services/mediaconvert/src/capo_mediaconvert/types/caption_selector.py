"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CaptionSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_min3_max3_pattern_a_za_z3
    import capo_mediaconvert.types.caption_source_settings
    import capo_mediaconvert.types.language_code


class CaptionSelector(TypedDict, closed=True):
    custom_language_code: NotRequired[
        "capo_mediaconvert.types.__string_min3_max3_pattern_a_za_z3.__stringMin3Max3PatternAZaZ3"
    ]
    """The specific language to extract from source, using the ISO 639-2 or ISO 639-3 three-letter language code. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions."""
    language_code: NotRequired["capo_mediaconvert.types.language_code.LanguageCode"]
    """The specific language to extract from source. If input is SCTE-27, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub and output is Burn-in, complete this field and/or PID to select the caption language to extract. If input is DVB-Sub that is being passed through, omit this field (and PID field); there is no way to extract a specific language with pass-through captions."""
    source_settings: NotRequired[
        "capo_mediaconvert.types.caption_source_settings.CaptionSourceSettings"
    ]
    """If your input captions are SCC, TTML, STL, SMI, SRT, or IMSC in an xml file, specify the URI of the input captions source file. If your input captions are IMSC in an IMF package, use TrackSourceSettings instead of FileSoureSettings."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSelector) -> dict:
    out: dict = {}
    if "custom_language_code" in value:
        out["customLanguageCode"] = value["custom_language_code"]
    if "language_code" in value:
        import capo_mediaconvert.types.language_code

        out["languageCode"] = capo_mediaconvert.types.language_code.serialize_json(
            value["language_code"]
        )
    if "source_settings" in value:
        import capo_mediaconvert.types.caption_source_settings

        out["sourceSettings"] = (
            capo_mediaconvert.types.caption_source_settings.serialize_json(
                value["source_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CaptionSelector:
    out: CaptionSelector = {}  # type: ignore[typeddict-item]
    if "customLanguageCode" in data:
        out["custom_language_code"] = data["customLanguageCode"]
    if "languageCode" in data:
        import capo_mediaconvert.types.language_code

        out["language_code"] = capo_mediaconvert.types.language_code.deserialize_json(
            data["languageCode"]
        )
    if "sourceSettings" in data:
        import capo_mediaconvert.types.caption_source_settings

        out["source_settings"] = (
            capo_mediaconvert.types.caption_source_settings.deserialize_json(
                data["sourceSettings"]
            )
        )
    return out
