"""Generated from Smithy shape ``com.amazonaws.comprehend#UnsupportedLanguageException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_comprehend.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.string


class UnsupportedLanguageException_(TypedDict):
    message: NotRequired["aws_sdk_comprehend.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedLanguageException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedLanguageException_:
    out: UnsupportedLanguageException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedLanguageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.comprehend#UnsupportedLanguageException``."""

    code: str | None = "UnsupportedLanguageException"

    def __init__(self, data: UnsupportedLanguageException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedLanguageException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedLanguageException":
        return cls(deserialize_aws_json_1_1(data))
