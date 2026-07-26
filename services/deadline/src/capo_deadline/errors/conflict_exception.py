"""Generated from Smithy shape ``com.amazonaws.deadline#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_deadline.types.conflict_exception_reason
    import capo_deadline.types.exception_context
    import capo_deadline.types.string


class ConflictException_(TypedDict, closed=True):
    message: "capo_deadline.types.string.String"
    reason: "capo_deadline.types.conflict_exception_reason.ConflictExceptionReason"
    """<p>A description of the error.</p>"""
    resource_id: "capo_deadline.types.string.String"
    """<p>The identifier of the resource in use.</p>"""
    resource_type: "capo_deadline.types.string.String"
    """<p>The type of the resource in use.</p>"""
    context: NotRequired["capo_deadline.types.exception_context.ExceptionContext"]
    """<p>Information about the resources in use when the exception was thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_deadline.types.conflict_exception_reason

    out["reason"] = capo_deadline.types.conflict_exception_reason.serialize_json(
        value["reason"]
    )
    out["resourceId"] = value["resource_id"]
    out["resourceType"] = value["resource_type"]
    if "context" in value:
        import capo_deadline.types.exception_context

        out["context"] = capo_deadline.types.exception_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    if "reason" in data:
        import capo_deadline.types.conflict_exception_reason

        out["reason"] = capo_deadline.types.conflict_exception_reason.deserialize_json(
            data["reason"]
        )
    else:
        raise DeserializationError("ConflictException_.reason required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("ConflictException_.resource_id required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ConflictException_.resource_type required")
    if "context" in data:
        import capo_deadline.types.exception_context

        out["context"] = capo_deadline.types.exception_context.deserialize_json(
            data["context"]
        )
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.deadline#ConflictException``."""

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
