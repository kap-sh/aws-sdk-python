"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#UnsupportedMediaTypeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_runtime_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.string


class UnsupportedMediaTypeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_lex_runtime_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedMediaTypeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedMediaTypeException_:
    out: UnsupportedMediaTypeException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedMediaTypeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimeservice#UnsupportedMediaTypeException``."""

    code: str | None = "UnsupportedMediaTypeException"

    def __init__(self, data: UnsupportedMediaTypeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedMediaTypeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnsupportedMediaTypeException":
        return cls(deserialize_json(data))
