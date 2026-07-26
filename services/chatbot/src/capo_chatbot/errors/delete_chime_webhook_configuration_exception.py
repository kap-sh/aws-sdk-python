"""Generated from Smithy shape ``com.amazonaws.chatbot#DeleteChimeWebhookConfigurationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import capo_chatbot.types.error_message


class DeleteChimeWebhookConfigurationException_(TypedDict, closed=True):
    message: NotRequired["capo_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChimeWebhookConfigurationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteChimeWebhookConfigurationException_:
    out: DeleteChimeWebhookConfigurationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DeleteChimeWebhookConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#DeleteChimeWebhookConfigurationException``."""

    code: str | None = "DeleteChimeWebhookConfigurationException"

    def __init__(self, data: DeleteChimeWebhookConfigurationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DeleteChimeWebhookConfigurationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeleteChimeWebhookConfigurationException":
        return cls(deserialize_json(data))
