"""Generated from Smithy shape ``com.amazonaws.connect#ConditionalOperationFailedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.message


class ConditionalOperationFailedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_connect.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalOperationFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConditionalOperationFailedException_:
    out: ConditionalOperationFailedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConditionalOperationFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#ConditionalOperationFailedException``."""

    code: str | None = "ConditionalOperationFailedException"

    def __init__(self, data: ConditionalOperationFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConditionalOperationFailedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConditionalOperationFailedException":
        return cls(deserialize_json(data))
