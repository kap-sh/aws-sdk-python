"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateTeamsChannelConfigurationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class UpdateTeamsChannelConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTeamsChannelConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UpdateTeamsChannelConfigurationException_:
    out: UpdateTeamsChannelConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UpdateTeamsChannelConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#UpdateTeamsChannelConfigurationException``."""

    code: str | None = "UpdateTeamsChannelConfigurationException"

    def __init__(self, data: UpdateTeamsChannelConfigurationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="UpdateTeamsChannelConfigurationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UpdateTeamsChannelConfigurationException":
        return cls(deserialize_json(data))
