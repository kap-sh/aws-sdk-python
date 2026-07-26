"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#NotManagementAccountException``."""

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer_automation.errors import ServiceError


class NotManagementAccountException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotManagementAccountException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NotManagementAccountException_:
    out: NotManagementAccountException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NotManagementAccountException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.computeoptimizerautomation#NotManagementAccountException``."""

    code: str | None = "NotManagementAccountException"

    def __init__(self, data: NotManagementAccountException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotManagementAccountException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "NotManagementAccountException":
        return cls(deserialize_aws_json_1_0(data))
