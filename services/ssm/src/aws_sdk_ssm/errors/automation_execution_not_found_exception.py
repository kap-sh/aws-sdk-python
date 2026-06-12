"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationExecutionNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class AutomationExecutionNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutomationExecutionNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutomationExecutionNotFoundException_:
    out: AutomationExecutionNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AutomationExecutionNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AutomationExecutionNotFoundException``."""

    code: str | None = "AutomationExecutionNotFoundException"

    def __init__(self, data: AutomationExecutionNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AutomationExecutionNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AutomationExecutionNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
