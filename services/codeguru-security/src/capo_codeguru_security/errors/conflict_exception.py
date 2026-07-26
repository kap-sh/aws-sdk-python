"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ConflictException``."""

from typing_extensions import TypedDict

from capo_codeguru_security.errors import DeserializationError, ServiceError


class ConflictException_(TypedDict, closed=True):
    error_code: "str"
    """<p>The identifier for the error.</p>"""
    message: "str"
    """<p>Description of the error.</p>"""
    resource_id: "str"
    """<p>The identifier for the service resource associated with the request.</p>"""
    resource_type: "str"
    """<p>The type of resource associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
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
    else:
        raise DeserializationError("ConflictException_.message required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codegurusecurity#ConflictException``."""

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
