"""Generated from Smithy shape ``com.amazonaws.translate#UnsupportedLanguagePairException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_translate.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_translate.types.language_code_string
    import aws_sdk_translate.types.string


class UnsupportedLanguagePairException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_translate.types.string.String"]
    source_language_code: NotRequired[
        "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The language code for the language of the input text. </p>"""
    target_language_code: NotRequired[
        "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The language code for the language of the translated text. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedLanguagePairException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_code" in value:
        out["TargetLanguageCode"] = value["target_language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedLanguagePairException_:
    out: UnsupportedLanguagePairException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "SourceLanguageCode" in data:
        out["source_language_code"] = data["SourceLanguageCode"]
    if "TargetLanguageCode" in data:
        out["target_language_code"] = data["TargetLanguageCode"]
    return out


class UnsupportedLanguagePairException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#UnsupportedLanguagePairException``."""

    code: str | None = "UnsupportedLanguagePairException"

    def __init__(self, data: UnsupportedLanguagePairException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedLanguagePairException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedLanguagePairException":
        return cls(deserialize_aws_json_1_1(data))
