"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ModelNotReadyException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.non_blank_string


class ModelNotReadyException_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ModelNotReadyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ModelNotReadyException_:
    out: ModelNotReadyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ModelNotReadyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentruntime#ModelNotReadyException``."""

    code: str | None = "ModelNotReadyException"

    def __init__(self, data: ModelNotReadyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelNotReadyException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ModelNotReadyException":
        return cls(deserialize_json(data))
