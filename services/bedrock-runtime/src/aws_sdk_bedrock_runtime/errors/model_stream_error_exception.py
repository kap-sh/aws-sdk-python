"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ModelStreamErrorException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.non_blank_string
    import aws_sdk_bedrock_runtime.types.status_code


class ModelStreamErrorException_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_runtime.types.non_blank_string.NonBlankString"
    ]
    original_status_code: NotRequired[
        "aws_sdk_bedrock_runtime.types.status_code.StatusCode"
    ]
    """<p>The original status code.</p>"""
    original_message: NotRequired[
        "aws_sdk_bedrock_runtime.types.non_blank_string.NonBlankString"
    ]
    """<p>The original message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelStreamErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "original_status_code" in value:
        out["originalStatusCode"] = value["original_status_code"]
    if "original_message" in value:
        out["originalMessage"] = value["original_message"]
    return out


def deserialize_json(data: dict) -> ModelStreamErrorException_:
    out: ModelStreamErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "originalStatusCode" in data:
        out["original_status_code"] = data["originalStatusCode"]
    if "originalMessage" in data:
        out["original_message"] = data["originalMessage"]
    return out


class ModelStreamErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockruntime#ModelStreamErrorException``."""

    code: str | None = "ModelStreamErrorException"

    def __init__(self, data: ModelStreamErrorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelStreamErrorException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ModelStreamErrorException":
        return cls(deserialize_json(data))
