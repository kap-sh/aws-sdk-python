"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.non_blank_string


class ValidationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.non_blank_string.NonBlankString"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ValidationException":
        return cls(deserialize_aws_json_1_1(data))
