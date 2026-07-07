"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorAuthenticationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.error_message


class ConnectorAuthenticationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appflow.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorAuthenticationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConnectorAuthenticationException_:
    out: ConnectorAuthenticationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConnectorAuthenticationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appflow#ConnectorAuthenticationException``."""

    code: str | None = "ConnectorAuthenticationException"

    def __init__(self, data: ConnectorAuthenticationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConnectorAuthenticationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConnectorAuthenticationException":
        return cls(deserialize_json(data))
