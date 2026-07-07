"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#BadGatewayException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_runtime_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.error_message


class BadGatewayException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_lex_runtime_service.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: BadGatewayException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadGatewayException_:
    out: BadGatewayException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BadGatewayException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexruntimeservice#BadGatewayException``."""

    code: str | None = "BadGatewayException"

    def __init__(self, data: BadGatewayException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="BadGatewayException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadGatewayException":
        return cls(deserialize_json(data))
