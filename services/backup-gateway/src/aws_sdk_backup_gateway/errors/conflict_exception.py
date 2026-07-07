"""Generated from Smithy shape ``com.amazonaws.backupgateway#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backup_gateway.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.string


class ConflictException_(TypedDict, closed=True):
    error_code: "aws_sdk_backup_gateway.types.string.string"
    """<p>A description of why the operation is not supported.</p>"""
    message: NotRequired["aws_sdk_backup_gateway.types.string.string"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConflictException_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("ConflictException_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backupgateway#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "ConflictException":
        return cls(deserialize_aws_json_1_0(data))
