"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RuntimeClientError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.non_blank_string


class RuntimeClientError_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_agentcore.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeClientError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RuntimeClientError_:
    out: RuntimeClientError_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RuntimeClientError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#RuntimeClientError``."""

    code: str | None = "RuntimeClientError"

    def __init__(self, data: RuntimeClientError_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RuntimeClientError",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RuntimeClientError":
        return cls(deserialize_json(data))
