"""Generated from Smithy shape ``com.amazonaws.translate#Language``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.language_code_string
    import aws_sdk_translate.types.localized_name_string


class Language(TypedDict):
    language_name: "aws_sdk_translate.types.localized_name_string.LocalizedNameString"
    """<p>Language name of the supported language.</p>"""
    language_code: "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    """<p>Language code for the supported language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Language) -> dict:
    out: dict = {}
    out["LanguageName"] = value["language_name"]
    out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Language:
    out: Language = {}  # type: ignore[typeddict-item]
    if "LanguageName" in data:
        out["language_name"] = data["LanguageName"]
    else:
        raise DeserializationError("Language.language_name required")
    if "LanguageCode" in data:
        out["language_code"] = data["LanguageCode"]
    else:
        raise DeserializationError("Language.language_code required")
    return out
