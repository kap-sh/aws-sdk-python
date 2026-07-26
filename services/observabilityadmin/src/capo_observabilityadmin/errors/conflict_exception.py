"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ConflictException``."""

from typing_extensions import NotRequired, TypedDict

from capo_observabilityadmin.errors import ServiceError


class ConflictException_(TypedDict, closed=True):
    message: NotRequired["str"]
    resource_id: NotRequired["str"]
    """<p> The identifier of the resource which is in conflict with the requested operation. </p>"""
    resource_type: NotRequired["str"]
    """<p> The type of the resource which is in conflict with the requested operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.observabilityadmin#ConflictException``."""

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
