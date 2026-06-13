"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ModelTimeoutException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.non_blank_string


class ModelTimeoutException_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_runtime.types.non_blank_string.NonBlankString"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ModelTimeoutException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ModelTimeoutException_:
    out: ModelTimeoutException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ModelTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockruntime#ModelTimeoutException``."""

    code: str | None = "ModelTimeoutException"

    def __init__(self, data: ModelTimeoutException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelTimeoutException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ModelTimeoutException":
        return cls(deserialize_json(data))
