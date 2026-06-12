"""Generated from Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsConfiguredTeamsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class ListMicrosoftTeamsConfiguredTeamsException_(TypedDict):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrosoftTeamsConfiguredTeamsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ListMicrosoftTeamsConfiguredTeamsException_:
    out: ListMicrosoftTeamsConfiguredTeamsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ListMicrosoftTeamsConfiguredTeamsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsConfiguredTeamsException``."""

    code: str | None = "ListMicrosoftTeamsConfiguredTeamsException"

    def __init__(self, data: ListMicrosoftTeamsConfiguredTeamsException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ListMicrosoftTeamsConfiguredTeamsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ListMicrosoftTeamsConfiguredTeamsException":
        return cls(deserialize_json(data))
