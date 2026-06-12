"""Generated from Smithy shape ``com.amazonaws.workdocs#InvalidCommentOperationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type


class InvalidCommentOperationException_(TypedDict):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidCommentOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidCommentOperationException_:
    out: InvalidCommentOperationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidCommentOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#InvalidCommentOperationException``."""

    code: str | None = "InvalidCommentOperationException"

    def __init__(self, data: InvalidCommentOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCommentOperationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidCommentOperationException":
        return cls(deserialize_json(data))
