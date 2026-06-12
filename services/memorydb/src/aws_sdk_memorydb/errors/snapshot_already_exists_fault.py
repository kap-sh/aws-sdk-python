"""Generated from Smithy shape ``com.amazonaws.memorydb#SnapshotAlreadyExistsFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.exception_message


class SnapshotAlreadyExistsFault_(TypedDict):
    message: NotRequired["aws_sdk_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotAlreadyExistsFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotAlreadyExistsFault_:
    out: SnapshotAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SnapshotAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#SnapshotAlreadyExistsFault``."""

    code: str | None = "SnapshotAlreadyExistsFault"

    def __init__(self, data: SnapshotAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SnapshotAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SnapshotAlreadyExistsFault":
        return cls(deserialize_aws_json_1_1(data))
