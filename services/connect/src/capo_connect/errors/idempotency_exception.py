"""Generated from Smithy shape ``com.amazonaws.connect#IdempotencyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import ServiceError

if TYPE_CHECKING:
    import capo_connect.types.message


class IdempotencyException_(TypedDict, closed=True):
    message: NotRequired["capo_connect.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: IdempotencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> IdempotencyException_:
    out: IdempotencyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class IdempotencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#IdempotencyException``."""

    code: str | None = "IdempotencyException"

    def __init__(self, data: IdempotencyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotencyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "IdempotencyException":
        return cls(deserialize_json(data))
