"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ConnectorFailureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import ServiceError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.error_message


class ConnectorFailureException_(TypedDict, closed=True):
    message: NotRequired["capo_iottwinmaker.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorFailureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConnectorFailureException_:
    out: ConnectorFailureException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ConnectorFailureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iottwinmaker#ConnectorFailureException``."""

    code: str | None = "ConnectorFailureException"

    def __init__(self, data: ConnectorFailureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConnectorFailureException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConnectorFailureException":
        return cls(deserialize_json(data))
