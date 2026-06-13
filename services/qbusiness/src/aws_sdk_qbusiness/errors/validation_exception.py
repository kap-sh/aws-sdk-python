"""Generated from Smithy shape ``com.amazonaws.qbusiness#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.error_message
    import aws_sdk_qbusiness.types.validation_exception_fields
    import aws_sdk_qbusiness.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: "aws_sdk_qbusiness.types.error_message.ErrorMessage"
    """<p>The message describing the <code>ValidationException</code>.</p>"""
    reason: (
        "aws_sdk_qbusiness.types.validation_exception_reason.ValidationExceptionReason"
    )
    """<p>The reason for the <code>ValidationException</code>.</p>"""
    fields: NotRequired[
        "aws_sdk_qbusiness.types.validation_exception_fields.ValidationExceptionFields"
    ]
    """<p>The input field(s) that failed validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_qbusiness.types.validation_exception_reason

    out["reason"] = aws_sdk_qbusiness.types.validation_exception_reason.serialize_json(
        value["reason"]
    )
    if "fields" in value:
        import aws_sdk_qbusiness.types.validation_exception_fields

        out["fields"] = (
            aws_sdk_qbusiness.types.validation_exception_fields.serialize_json(
                value["fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "reason" in data:
        import aws_sdk_qbusiness.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_qbusiness.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "fields" in data:
        import aws_sdk_qbusiness.types.validation_exception_fields

        out["fields"] = (
            aws_sdk_qbusiness.types.validation_exception_fields.deserialize_json(
                data["fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qbusiness#ValidationException``."""

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
