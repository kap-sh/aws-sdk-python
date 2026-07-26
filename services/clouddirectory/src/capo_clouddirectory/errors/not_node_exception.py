"""Generated from Smithy shape ``com.amazonaws.clouddirectory#NotNodeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import capo_clouddirectory.types.exception_message


class NotNodeException_(TypedDict, closed=True):
    message: NotRequired["capo_clouddirectory.types.exception_message.ExceptionMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: NotNodeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotNodeException_:
    out: NotNodeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class NotNodeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#NotNodeException``."""

    code: str | None = "NotNodeException"

    def __init__(self, data: NotNodeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotNodeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotNodeException":
        return cls(deserialize_json(data))
