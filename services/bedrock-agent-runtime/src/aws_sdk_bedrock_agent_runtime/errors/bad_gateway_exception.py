"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BadGatewayException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_agent_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.non_blank_string


class BadGatewayException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]
    resource_name: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]
    """<p>The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or STS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BadGatewayException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> BadGatewayException_:
    out: BadGatewayException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out


class BadGatewayException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentruntime#BadGatewayException``."""

    code: str | None = "BadGatewayException"

    def __init__(self, data: BadGatewayException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="BadGatewayException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadGatewayException":
        return cls(deserialize_json(data))


def serialize_event_json(value: BadGatewayException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "badGatewayException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> BadGatewayException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: BadGatewayException_ = {}  # type: ignore[typeddict-item]
    return out
