"""Generated from Smithy shape ``com.amazonaws.deadline#AccessDeniedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.exception_context
    import aws_sdk_deadline.types.string


class AccessDeniedException_(TypedDict, closed=True):
    message: "aws_sdk_deadline.types.string.String"
    context: NotRequired["aws_sdk_deadline.types.exception_context.ExceptionContext"]
    """<p>Information about the resources in use when the exception was thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    if "context" in value:
        import aws_sdk_deadline.types.exception_context

        out["context"] = aws_sdk_deadline.types.exception_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    if "context" in data:
        import aws_sdk_deadline.types.exception_context

        out["context"] = aws_sdk_deadline.types.exception_context.deserialize_json(
            data["context"]
        )
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.deadline#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))
