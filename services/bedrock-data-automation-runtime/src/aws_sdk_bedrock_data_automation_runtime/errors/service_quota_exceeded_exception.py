"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation_runtime.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.non_blank_string


class ServiceQuotaExceededException_(TypedDict):
    message: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.non_blank_string.NonBlankString"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockdataautomationruntime#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(self, data: ServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_aws_json_1_1(data))
