"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ModelErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.non_blank_string
    import aws_sdk_bedrock_runtime.types.status_code


class ModelErrorException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_bedrock_runtime.types.non_blank_string.NonBlankString"
    ]
    original_status_code: NotRequired[
        "aws_sdk_bedrock_runtime.types.status_code.StatusCode"
    ]
    """<p>The original status code.</p>"""
    resource_name: NotRequired[
        "aws_sdk_bedrock_runtime.types.non_blank_string.NonBlankString"
    ]
    """<p>The resource name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelErrorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "original_status_code" in value:
        out["originalStatusCode"] = value["original_status_code"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> ModelErrorException_:
    out: ModelErrorException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "originalStatusCode" in data:
        out["original_status_code"] = data["originalStatusCode"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out


class ModelErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockruntime#ModelErrorException``."""

    code: str | None = "ModelErrorException"

    def __init__(self, data: ModelErrorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ModelErrorException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ModelErrorException":
        return cls(deserialize_json(data))
