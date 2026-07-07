"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteMicrosoftTeamsUserIdentityException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class DeleteMicrosoftTeamsUserIdentityException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMicrosoftTeamsUserIdentityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteMicrosoftTeamsUserIdentityException_:
    out: DeleteMicrosoftTeamsUserIdentityException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DeleteMicrosoftTeamsUserIdentityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#DeleteMicrosoftTeamsUserIdentityException``."""

    code: str | None = "DeleteMicrosoftTeamsUserIdentityException"

    def __init__(self, data: DeleteMicrosoftTeamsUserIdentityException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DeleteMicrosoftTeamsUserIdentityException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeleteMicrosoftTeamsUserIdentityException":
        return cls(deserialize_json(data))
