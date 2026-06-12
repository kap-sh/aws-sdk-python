"""Generated from Smithy shape ``com.amazonaws.translate#TextSizeLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_translate.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_translate.types.string


class TextSizeLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_translate.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextSizeLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TextSizeLimitExceededException_:
    out: TextSizeLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TextSizeLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.translate#TextSizeLimitExceededException``."""

    code: str | None = "TextSizeLimitExceededException"

    def __init__(self, data: TextSizeLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TextSizeLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TextSizeLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
