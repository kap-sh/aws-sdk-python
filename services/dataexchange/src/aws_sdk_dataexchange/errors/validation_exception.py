"""Generated from Smithy shape ``com.amazonaws.dataexchange#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.exception_cause


class ValidationException_(TypedDict, closed=True):
    message: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The message that informs you about what was invalid about the request.</p>"""
    exception_cause: NotRequired[
        "aws_sdk_dataexchange.types.exception_cause.ExceptionCause"
    ]
    """<p>The unique identifier for the resource that couldn't be found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "exception_cause" in value:
        out["ExceptionCause"] = value["exception_cause"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "ExceptionCause" in data:
        out["exception_cause"] = data["ExceptionCause"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dataexchange#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ValidationException":
        return cls(deserialize_json(data))
