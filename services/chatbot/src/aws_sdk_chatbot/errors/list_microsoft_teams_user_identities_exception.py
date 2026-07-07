"""Generated from Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsUserIdentitiesException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class ListMicrosoftTeamsUserIdentitiesException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrosoftTeamsUserIdentitiesException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ListMicrosoftTeamsUserIdentitiesException_:
    out: ListMicrosoftTeamsUserIdentitiesException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ListMicrosoftTeamsUserIdentitiesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#ListMicrosoftTeamsUserIdentitiesException``."""

    code: str | None = "ListMicrosoftTeamsUserIdentitiesException"

    def __init__(self, data: ListMicrosoftTeamsUserIdentitiesException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ListMicrosoftTeamsUserIdentitiesException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ListMicrosoftTeamsUserIdentitiesException":
        return cls(deserialize_json(data))
