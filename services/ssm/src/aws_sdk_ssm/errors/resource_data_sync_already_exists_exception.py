"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_name


class ResourceDataSyncAlreadyExistsException_(TypedDict, closed=True):
    sync_name: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncAlreadyExistsException_) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncAlreadyExistsException_:
    out: ResourceDataSyncAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "SyncName" in data:
        out["sync_name"] = data["SyncName"]
    return out


class ResourceDataSyncAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourceDataSyncAlreadyExistsException``."""

    code: str | None = "ResourceDataSyncAlreadyExistsException"

    def __init__(self, data: ResourceDataSyncAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDataSyncAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceDataSyncAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
