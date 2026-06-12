"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotNotFound``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message


class SnapshotNotFound_(TypedDict):
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotNotFound_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotNotFound_:
    out: SnapshotNotFound_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class SnapshotNotFound(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#SnapshotNotFound``."""

    code: str | None = "SnapshotNotFound"

    def __init__(self, data: SnapshotNotFound_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SnapshotNotFound",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SnapshotNotFound":
        return cls(deserialize_aws_json_1_1(data))
