"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#DuplicatedAuditEventId``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail_data.errors import ServiceError


class DuplicatedAuditEventId_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DuplicatedAuditEventId_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DuplicatedAuditEventId_:
    out: DuplicatedAuditEventId_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DuplicatedAuditEventId(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtraildata#DuplicatedAuditEventId``."""

    code: str | None = "DuplicatedAuditEventId"

    def __init__(self, data: DuplicatedAuditEventId_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicatedAuditEventId",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DuplicatedAuditEventId":
        return cls(deserialize_json(data))
