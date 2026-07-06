"""Generated from Smithy shape ``com.amazonaws.backupgateway#InternalServerException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backup_gateway.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.string


class InternalServerException_(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_backup_gateway.types.string.string"]
    """<p>A description of which internal error occured.</p>"""
    message: NotRequired["aws_sdk_backup_gateway.types.string.string"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InternalServerException_) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InternalServerException_:
    out: InternalServerException_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.backupgateway#InternalServerException``."""

    code: str | None = "InternalServerException"

    def __init__(self, data: InternalServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InternalServerException":
        return cls(deserialize_aws_json_1_0(data))
