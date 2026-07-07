"""Generated from Smithy shape ``com.amazonaws.translate#UnsupportedDisplayLanguageCodeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_translate.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_translate.types.language_code_string
    import aws_sdk_translate.types.string


class UnsupportedDisplayLanguageCodeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_translate.types.string.String"]
    display_language_code: NotRequired[
        "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>Language code passed in with the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedDisplayLanguageCodeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "display_language_code" in value:
        out["DisplayLanguageCode"] = value["display_language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedDisplayLanguageCodeException_:
    out: UnsupportedDisplayLanguageCodeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "DisplayLanguageCode" in data:
        out["display_language_code"] = data["DisplayLanguageCode"]
    return out


class UnsupportedDisplayLanguageCodeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#UnsupportedDisplayLanguageCodeException``."""

    code: str | None = "UnsupportedDisplayLanguageCodeException"

    def __init__(self, data: UnsupportedDisplayLanguageCodeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedDisplayLanguageCodeException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedDisplayLanguageCodeException":
        return cls(deserialize_aws_json_1_1(data))
