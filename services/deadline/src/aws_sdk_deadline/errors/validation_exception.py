"""Generated from Smithy shape ``com.amazonaws.deadline#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.exception_context
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.validation_exception_field_list
    import aws_sdk_deadline.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: "aws_sdk_deadline.types.string.String"
    reason: (
        "aws_sdk_deadline.types.validation_exception_reason.ValidationExceptionReason"
    )
    """<p>The reason that the request failed validation.</p>"""
    field_list: NotRequired[
        "aws_sdk_deadline.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>A list of fields that failed validation.</p>"""
    context: NotRequired["aws_sdk_deadline.types.exception_context.ExceptionContext"]
    """<p>Information about the resources in use when the exception was thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_deadline.types.validation_exception_reason

    out["reason"] = aws_sdk_deadline.types.validation_exception_reason.serialize_json(
        value["reason"]
    )
    if "field_list" in value:
        import aws_sdk_deadline.types.validation_exception_field_list

        out["fieldList"] = (
            aws_sdk_deadline.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    if "context" in value:
        import aws_sdk_deadline.types.exception_context

        out["context"] = aws_sdk_deadline.types.exception_context.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "reason" in data:
        import aws_sdk_deadline.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_deadline.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "fieldList" in data:
        import aws_sdk_deadline.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_deadline.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    if "context" in data:
        import aws_sdk_deadline.types.exception_context

        out["context"] = aws_sdk_deadline.types.exception_context.deserialize_json(
            data["context"]
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.deadline#ValidationException``."""

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
