"""Generated from Smithy shape ``com.amazonaws.fsx#BackupNotFound``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message


class BackupNotFound_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BackupNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BackupNotFound_:
    out: BackupNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BackupNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#BackupNotFound``."""

    code: str | None = "BackupNotFound"

    def __init__(self, data: BackupNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BackupNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BackupNotFound":
        return cls(deserialize_aws_json_1_1(data))
