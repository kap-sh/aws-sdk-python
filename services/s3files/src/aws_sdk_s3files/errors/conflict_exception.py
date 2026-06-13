"""Generated from Smithy shape ``com.amazonaws.s3files#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3files.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.error_code


class ConflictException_(TypedDict):
    error_code: "aws_sdk_s3files.types.error_code.ErrorCode"
    """<p>The error code associated with the exception.</p>"""
    message: NotRequired["str"]
    resource_id: NotRequired["str"]
    """<p>The identifier of the resource that caused the conflict.</p>"""
    resource_type: NotRequired["str"]
    """<p>The type of the resource that caused the conflict.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    if "message" in value:
        out["message"] = value["message"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ConflictException_.error_code required")
    if "message" in data:
        out["message"] = data["message"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3files#ConflictException``."""

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
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
