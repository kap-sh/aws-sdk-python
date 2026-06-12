"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentLockedForCommentsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workdocs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.error_message_type


class DocumentLockedForCommentsException_(TypedDict):
    message: NotRequired["aws_sdk_workdocs.types.error_message_type.ErrorMessageType"]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentLockedForCommentsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DocumentLockedForCommentsException_:
    out: DocumentLockedForCommentsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DocumentLockedForCommentsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workdocs#DocumentLockedForCommentsException``."""

    code: str | None = "DocumentLockedForCommentsException"

    def __init__(self, data: DocumentLockedForCommentsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DocumentLockedForCommentsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DocumentLockedForCommentsException":
        return cls(deserialize_json(data))
