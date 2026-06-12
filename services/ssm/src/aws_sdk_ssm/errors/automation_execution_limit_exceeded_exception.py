"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class AutomationExecutionLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecutionLimitExceededException_:
    out: AutomationExecutionLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AutomationExecutionLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AutomationExecutionLimitExceededException``."""

    code: str | None = "AutomationExecutionLimitExceededException"

    def __init__(self, data: AutomationExecutionLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AutomationExecutionLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "AutomationExecutionLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
