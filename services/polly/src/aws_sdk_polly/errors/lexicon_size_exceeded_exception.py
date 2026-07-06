"""Generated from Smithy shape ``com.amazonaws.polly#LexiconSizeExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_polly.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.error_message


class LexiconSizeExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: LexiconSizeExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LexiconSizeExceededException_:
    out: LexiconSizeExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class LexiconSizeExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#LexiconSizeExceededException``."""

    code: str | None = "LexiconSizeExceededException"

    def __init__(self, data: LexiconSizeExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LexiconSizeExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LexiconSizeExceededException":
        return cls(deserialize_json(data))
