"""Generated from Smithy shape ``com.amazonaws.chatbot#DescribeSlackWorkspacesException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.error_message


class DescribeSlackWorkspacesException_(TypedDict):
    message: NotRequired["aws_sdk_chatbot.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSlackWorkspacesException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DescribeSlackWorkspacesException_:
    out: DescribeSlackWorkspacesException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DescribeSlackWorkspacesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.chatbot#DescribeSlackWorkspacesException``."""

    code: str | None = "DescribeSlackWorkspacesException"

    def __init__(self, data: DescribeSlackWorkspacesException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DescribeSlackWorkspacesException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DescribeSlackWorkspacesException":
        return cls(deserialize_json(data))
