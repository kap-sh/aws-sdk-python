"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeguru_security.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.validation_exception_field_list
    import aws_sdk_codeguru_security.types.validation_exception_reason


class ValidationException_(TypedDict):
    error_code: "str"
    """<p>The identifier for the error.</p>"""
    message: "str"
    """<p>Description of the error.</p>"""
    reason: "aws_sdk_codeguru_security.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The reason the request failed validation.</p>"""
    field_list: NotRequired[
        "aws_sdk_codeguru_security.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The field that caused the error, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["message"] = value["message"]
    import aws_sdk_codeguru_security.types.validation_exception_reason

    out["reason"] = (
        aws_sdk_codeguru_security.types.validation_exception_reason.serialize_json(
            value["reason"]
        )
    )
    if "field_list" in value:
        import aws_sdk_codeguru_security.types.validation_exception_field_list

        out["fieldList"] = (
            aws_sdk_codeguru_security.types.validation_exception_field_list.serialize_json(
                value["field_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ValidationException_.error_code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "reason" in data:
        import aws_sdk_codeguru_security.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_codeguru_security.types.validation_exception_reason.deserialize_json(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "fieldList" in data:
        import aws_sdk_codeguru_security.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_codeguru_security.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codegurusecurity#ValidationException``."""

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
