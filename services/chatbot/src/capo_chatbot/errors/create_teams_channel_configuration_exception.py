"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateTeamsChannelConfigurationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class CreateTeamsChannelConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateTeamsChannelConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CreateTeamsChannelConfigurationException_:
    out: CreateTeamsChannelConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class CreateTeamsChannelConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#CreateTeamsChannelConfigurationException``."""

    code: str | None = "CreateTeamsChannelConfigurationException"

    def __init__(self, data: CreateTeamsChannelConfigurationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="CreateTeamsChannelConfigurationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "CreateTeamsChannelConfigurationException":
        return cls(deserialize_json(data))
