"""Generated from Smithy shape ``com.amazonaws.licensemanager#FailedDependencyException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.message
    import aws_sdk_license_manager.types.string


class FailedDependencyException_(TypedDict):
    message: NotRequired["aws_sdk_license_manager.types.message.Message"]
    error_code: NotRequired["aws_sdk_license_manager.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedDependencyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedDependencyException_:
    out: FailedDependencyException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    return out


class FailedDependencyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#FailedDependencyException``."""

    code: str | None = "FailedDependencyException"

    def __init__(self, data: FailedDependencyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FailedDependencyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FailedDependencyException":
        return cls(deserialize_aws_json_1_1(data))
