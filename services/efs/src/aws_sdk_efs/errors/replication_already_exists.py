"""Generated from Smithy shape ``com.amazonaws.efs#ReplicationAlreadyExists``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_efs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.error_code
    import aws_sdk_efs.types.error_message


class ReplicationAlreadyExists_(TypedDict):
    error_code: NotRequired["aws_sdk_efs.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationAlreadyExists_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ReplicationAlreadyExists_:
    out: ReplicationAlreadyExists_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ReplicationAlreadyExists(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#ReplicationAlreadyExists``."""

    code: str | None = "ReplicationAlreadyExists"

    def __init__(self, data: ReplicationAlreadyExists_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReplicationAlreadyExists",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ReplicationAlreadyExists":
        return cls(deserialize_json(data))
