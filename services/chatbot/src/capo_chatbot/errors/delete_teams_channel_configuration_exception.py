"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteTeamsChannelConfigurationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class DeleteTeamsChannelConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTeamsChannelConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteTeamsChannelConfigurationException_:
    out: DeleteTeamsChannelConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DeleteTeamsChannelConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#DeleteTeamsChannelConfigurationException``."""

    code: str | None = "DeleteTeamsChannelConfigurationException"

    def __init__(self, data: DeleteTeamsChannelConfigurationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DeleteTeamsChannelConfigurationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeleteTeamsChannelConfigurationException":
        return cls(deserialize_json(data))
