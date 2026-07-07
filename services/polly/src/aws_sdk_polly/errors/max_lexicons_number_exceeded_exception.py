"""Generated from Smithy shape ``com.amazonaws.polly#MaxLexiconsNumberExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_polly.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.error_message


class MaxLexiconsNumberExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MaxLexiconsNumberExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MaxLexiconsNumberExceededException_:
    out: MaxLexiconsNumberExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MaxLexiconsNumberExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#MaxLexiconsNumberExceededException``."""

    code: str | None = "MaxLexiconsNumberExceededException"

    def __init__(self, data: MaxLexiconsNumberExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaxLexiconsNumberExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MaxLexiconsNumberExceededException":
        return cls(deserialize_json(data))
