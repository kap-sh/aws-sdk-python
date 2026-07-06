"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ConnectorTimeoutException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.error_message


class ConnectorTimeoutException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_iottwinmaker.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConnectorTimeoutException_:
    out: ConnectorTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConnectorTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iottwinmaker#ConnectorTimeoutException``."""

    code: str | None = "ConnectorTimeoutException"

    def __init__(self, data: ConnectorTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConnectorTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConnectorTimeoutException":
        return cls(deserialize_json(data))
