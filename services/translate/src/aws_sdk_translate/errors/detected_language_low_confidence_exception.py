"""Generated from Smithy shape ``com.amazonaws.translate#DetectedLanguageLowConfidenceException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_translate.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_translate.types.language_code_string
    import aws_sdk_translate.types.string


class DetectedLanguageLowConfidenceException_(TypedDict):
    message: NotRequired["aws_sdk_translate.types.string.String"]
    detected_language_code: NotRequired[
        "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The language code of the auto-detected language from Amazon Comprehend.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectedLanguageLowConfidenceException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "detected_language_code" in value:
        out["DetectedLanguageCode"] = value["detected_language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectedLanguageLowConfidenceException_:
    out: DetectedLanguageLowConfidenceException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "DetectedLanguageCode" in data:
        out["detected_language_code"] = data["DetectedLanguageCode"]
    return out


class DetectedLanguageLowConfidenceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#DetectedLanguageLowConfidenceException``."""

    code: str | None = "DetectedLanguageLowConfidenceException"

    def __init__(self, data: DetectedLanguageLowConfidenceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DetectedLanguageLowConfidenceException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DetectedLanguageLowConfidenceException":
        return cls(deserialize_aws_json_1_1(data))
