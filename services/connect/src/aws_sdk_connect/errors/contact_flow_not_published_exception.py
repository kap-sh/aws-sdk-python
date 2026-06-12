"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowNotPublishedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.message


class ContactFlowNotPublishedException_(TypedDict):
    message: NotRequired["aws_sdk_connect.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowNotPublishedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ContactFlowNotPublishedException_:
    out: ContactFlowNotPublishedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ContactFlowNotPublishedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#ContactFlowNotPublishedException``."""

    code: str | None = "ContactFlowNotPublishedException"

    def __init__(self, data: ContactFlowNotPublishedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContactFlowNotPublishedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ContactFlowNotPublishedException":
        return cls(deserialize_json(data))
