"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#MessageFrozen``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmailmessageflow.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workmailmessageflow.types.error_message


class MessageFrozen_(TypedDict):
    message: NotRequired["aws_sdk_workmailmessageflow.types.error_message.errorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: MessageFrozen_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MessageFrozen_:
    out: MessageFrozen_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MessageFrozen(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmailmessageflow#MessageFrozen``."""

    code: str | None = "MessageFrozen"

    def __init__(self, data: MessageFrozen_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MessageFrozen",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MessageFrozen":
        return cls(deserialize_json(data))
