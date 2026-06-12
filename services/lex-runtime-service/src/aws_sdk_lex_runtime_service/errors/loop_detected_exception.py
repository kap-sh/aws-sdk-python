"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#LoopDetectedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_runtime_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.error_message


class LoopDetectedException_(TypedDict):
    message: NotRequired["aws_sdk_lex_runtime_service.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: LoopDetectedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> LoopDetectedException_:
    out: LoopDetectedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class LoopDetectedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimeservice#LoopDetectedException``."""

    code: str | None = "LoopDetectedException"

    def __init__(self, data: LoopDetectedException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="LoopDetectedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LoopDetectedException":
        return cls(deserialize_json(data))
