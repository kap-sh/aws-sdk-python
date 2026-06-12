"""Generated from Smithy shape ``com.amazonaws.novaact#ConflictException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.non_blank_string


class ConflictException_(TypedDict):
    message: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The requested operation conflicts with the current state of the resource.</p>"""
    resource_id: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The identifier of the resource that caused the conflict.</p>"""
    resource_type: "aws_sdk_nova_act.types.non_blank_string.NonBlankString"
    """<p>The type of resource that caused the conflict.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
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
    """Modeled error for Smithy shape ``com.amazonaws.novaact#ConflictException``."""

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
