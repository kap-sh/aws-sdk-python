"""Generated from Smithy shape ``com.amazonaws.licensemanager#ResourceLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_license_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_license_manager.types.message


class ResourceLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_license_manager.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceLimitExceededException_:
    out: ResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.licensemanager#ResourceLimitExceededException``."""

    code: str | None = "ResourceLimitExceededException"

    def __init__(self, data: ResourceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
