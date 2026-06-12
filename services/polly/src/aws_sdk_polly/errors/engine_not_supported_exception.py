"""Generated from Smithy shape ``com.amazonaws.polly#EngineNotSupportedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_polly.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.error_message


class EngineNotSupportedException_(TypedDict):
    message: NotRequired["aws_sdk_polly.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: EngineNotSupportedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EngineNotSupportedException_:
    out: EngineNotSupportedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class EngineNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#EngineNotSupportedException``."""

    code: str | None = "EngineNotSupportedException"

    def __init__(self, data: EngineNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EngineNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "EngineNotSupportedException":
        return cls(deserialize_json(data))
