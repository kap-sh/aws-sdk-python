"""Generated from Smithy shape ``com.amazonaws.fsx#BackupBeingCopied``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.backup_id
    import aws_sdk_fsx.types.error_message


class BackupBeingCopied_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]
    backup_id: NotRequired["aws_sdk_fsx.types.backup_id.BackupId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupBeingCopied_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "backup_id" in value:
        out["BackupId"] = value["backup_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BackupBeingCopied_:
    out: BackupBeingCopied_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "BackupId" in data:
        out["backup_id"] = data["BackupId"]
    return out


class BackupBeingCopied(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#BackupBeingCopied``."""

    code: str | None = "BackupBeingCopied"

    def __init__(self, data: BackupBeingCopied_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BackupBeingCopied",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BackupBeingCopied":
        return cls(deserialize_aws_json_1_1(data))
