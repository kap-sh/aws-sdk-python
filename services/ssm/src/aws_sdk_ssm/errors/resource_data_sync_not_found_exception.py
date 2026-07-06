"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_name
    import aws_sdk_ssm.types.resource_data_sync_type
    import aws_sdk_ssm.types.string


class ResourceDataSyncNotFoundException_(TypedDict, closed=True):
    sync_name: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]
    sync_type: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    ]
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncNotFoundException_) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    if "sync_type" in value:
        out["SyncType"] = value["sync_type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncNotFoundException_:
    out: ResourceDataSyncNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "SyncName" in data:
        out["sync_name"] = data["SyncName"]
    if "SyncType" in data:
        out["sync_type"] = data["SyncType"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceDataSyncNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ResourceDataSyncNotFoundException``."""

    code: str | None = "ResourceDataSyncNotFoundException"

    def __init__(self, data: ResourceDataSyncNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceDataSyncNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceDataSyncNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
