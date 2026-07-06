"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class ResourceDataSyncConflictException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncConflictException_:
    out: ResourceDataSyncConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceDataSyncConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourceDataSyncConflictException``."""

    code: str | None = "ResourceDataSyncConflictException"

    def __init__(self, data: ResourceDataSyncConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDataSyncConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceDataSyncConflictException":
        return cls(deserialize_aws_json_1_1(data))
