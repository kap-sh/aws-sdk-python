"""Generated from Smithy shape ``com.amazonaws.polly#SsmlMarksNotSupportedForTextTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_polly.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.error_message


class SsmlMarksNotSupportedForTextTypeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: SsmlMarksNotSupportedForTextTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SsmlMarksNotSupportedForTextTypeException_:
    out: SsmlMarksNotSupportedForTextTypeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SsmlMarksNotSupportedForTextTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#SsmlMarksNotSupportedForTextTypeException``."""

    code: str | None = "SsmlMarksNotSupportedForTextTypeException"

    def __init__(self, data: SsmlMarksNotSupportedForTextTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SsmlMarksNotSupportedForTextTypeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "SsmlMarksNotSupportedForTextTypeException":
        return cls(deserialize_json(data))
