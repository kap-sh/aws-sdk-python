"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#InvalidNextTokenException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codestar_notifications.errors import ServiceError

if TYPE_CHECKING:
    import capo_codestar_notifications.types.message


class InvalidNextTokenException_(TypedDict, closed=True):
    message: NotRequired["capo_codestar_notifications.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidNextTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidNextTokenException_:
    out: InvalidNextTokenException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidNextTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codestarnotifications#InvalidNextTokenException``."""

    code: str | None = "InvalidNextTokenException"

    def __init__(self, data: InvalidNextTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNextTokenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidNextTokenException":
        return cls(deserialize_json(data))
