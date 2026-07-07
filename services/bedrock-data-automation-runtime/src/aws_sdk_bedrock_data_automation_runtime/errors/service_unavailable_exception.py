"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ServiceUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.non_blank_string


class ServiceUnavailableException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.non_blank_string.NonBlankString"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ServiceUnavailableException``."""

    code: str | None = "ServiceUnavailableException"

    def __init__(self, data: ServiceUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceUnavailableException":
        return cls(deserialize_aws_json_1_1(data))
