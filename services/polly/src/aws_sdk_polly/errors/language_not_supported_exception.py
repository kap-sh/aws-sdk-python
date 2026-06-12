"""Generated from Smithy shape ``com.amazonaws.polly#LanguageNotSupportedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_polly.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.error_message


class LanguageNotSupportedException_(TypedDict):
    message: NotRequired["aws_sdk_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: LanguageNotSupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LanguageNotSupportedException_:
    out: LanguageNotSupportedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class LanguageNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#LanguageNotSupportedException``."""

    code: str | None = "LanguageNotSupportedException"

    def __init__(self, data: LanguageNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LanguageNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LanguageNotSupportedException":
        return cls(deserialize_json(data))
