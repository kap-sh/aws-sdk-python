"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteTeamsConfiguredTeamException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class DeleteTeamsConfiguredTeamException_(TypedDict):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTeamsConfiguredTeamException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteTeamsConfiguredTeamException_:
    out: DeleteTeamsConfiguredTeamException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DeleteTeamsConfiguredTeamException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#DeleteTeamsConfiguredTeamException``."""

    code: str | None = "DeleteTeamsConfiguredTeamException"

    def __init__(self, data: DeleteTeamsConfiguredTeamException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DeleteTeamsConfiguredTeamException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeleteTeamsConfiguredTeamException":
        return cls(deserialize_json(data))
