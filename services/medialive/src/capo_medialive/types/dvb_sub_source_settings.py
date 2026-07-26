"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSubSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.dvb_sub_ocr_language


class DvbSubSourceSettings(TypedDict, closed=True):
    ocr_language: NotRequired[
        "capo_medialive.types.dvb_sub_ocr_language.DvbSubOcrLanguage"
    ]
    """If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text."""
    pid: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """When using DVB-Sub with Burn-In or SMPTE-TT, use this PID for the source content. Unused for DVB-Sub passthrough. All DVB-Sub content is passed through, regardless of selectors."""


# --- restJson1 ser/de ---
def serialize_json(value: DvbSubSourceSettings) -> dict:
    out: dict = {}
    if "ocr_language" in value:
        import capo_medialive.types.dvb_sub_ocr_language

        out["ocrLanguage"] = capo_medialive.types.dvb_sub_ocr_language.serialize_json(
            value["ocr_language"]
        )
    if "pid" in value:
        out["pid"] = value["pid"]
    return out


def deserialize_json(data: dict) -> DvbSubSourceSettings:
    out: DvbSubSourceSettings = {}  # type: ignore[typeddict-item]
    if "ocrLanguage" in data:
        import capo_medialive.types.dvb_sub_ocr_language

        out["ocr_language"] = (
            capo_medialive.types.dvb_sub_ocr_language.deserialize_json(
                data["ocrLanguage"]
            )
        )
    if "pid" in data:
        out["pid"] = data["pid"]
    return out
