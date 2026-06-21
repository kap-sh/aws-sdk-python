"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DependencyFailedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from aws_sdk_bedrock_agent_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.non_blank_string


class DependencyFailedException_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]
    resource_name: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]
    """<p>The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or STS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> DependencyFailedException_:
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out


class DependencyFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentruntime#DependencyFailedException``."""

    code: str | None = "DependencyFailedException"

    def __init__(self, data: DependencyFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyFailedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DependencyFailedException":
        return cls(deserialize_json(data))


def serialize_event_json(value: DependencyFailedException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "dependencyFailedException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> DependencyFailedException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    return out
