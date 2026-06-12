"""Generated from Smithy shape ``com.amazonaws.medialive#Scte27SourceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.scte27_ocr_language


class Scte27SourceSettings(TypedDict):
    ocr_language: NotRequired[
        "aws_sdk_medialive.types.scte27_ocr_language.Scte27OcrLanguage"
    ]
    """If you will configure a WebVTT caption description that references this caption selector, use this field to provide the language to consider when translating the image-based source to text."""
    pid: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    """The pid field is used in conjunction with the caption selector languageCode field as follows: - Specify PID and Language: Extracts captions from that PID; the language is \"informational\". - Specify PID and omit Language: Extracts the specified PID. - Omit PID and specify Language: Extracts the specified language, whichever PID that happens to be. - Omit PID and omit Language: Valid only if source is DVB-Sub that is being passed through; all languages will be passed through."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte27SourceSettings) -> dict:
    out: dict = {}
    if "ocr_language" in value:
        import aws_sdk_medialive.types.scte27_ocr_language

        out["ocrLanguage"] = aws_sdk_medialive.types.scte27_ocr_language.serialize_json(
            value["ocr_language"]
        )
    if "pid" in value:
        out["pid"] = value["pid"]
    return out


def deserialize_json(data: dict) -> Scte27SourceSettings:
    out: Scte27SourceSettings = {}  # type: ignore[typeddict-item]
    if "ocrLanguage" in data:
        import aws_sdk_medialive.types.scte27_ocr_language

        out["ocr_language"] = (
            aws_sdk_medialive.types.scte27_ocr_language.deserialize_json(
                data["ocrLanguage"]
            )
        )
    if "pid" in data:
        out["pid"] = data["pid"]
    return out
