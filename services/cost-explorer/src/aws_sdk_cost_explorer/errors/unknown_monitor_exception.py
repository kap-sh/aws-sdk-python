"""Generated from Smithy shape ``com.amazonaws.costexplorer#UnknownMonitorException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.error_message


class UnknownMonitorException_(TypedDict):
    message: NotRequired["aws_sdk_cost_explorer.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnknownMonitorException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnknownMonitorException_:
    out: UnknownMonitorException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnknownMonitorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costexplorer#UnknownMonitorException``."""

    code: str | None = "UnknownMonitorException"

    def __init__(self, data: UnknownMonitorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnknownMonitorException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnknownMonitorException":
        return cls(deserialize_aws_json_1_1(data))
