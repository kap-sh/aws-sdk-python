"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteSlackWorkspaceAuthorizationFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class DeleteSlackWorkspaceAuthorizationFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlackWorkspaceAuthorizationFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteSlackWorkspaceAuthorizationFault_:
    out: DeleteSlackWorkspaceAuthorizationFault_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DeleteSlackWorkspaceAuthorizationFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#DeleteSlackWorkspaceAuthorizationFault``."""

    code: str | None = "DeleteSlackWorkspaceAuthorizationFault"

    def __init__(self, data: DeleteSlackWorkspaceAuthorizationFault_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DeleteSlackWorkspaceAuthorizationFault",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeleteSlackWorkspaceAuthorizationFault":
        return cls(deserialize_json(data))
