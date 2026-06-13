"""Generated from Smithy shape ``com.amazonaws.billing#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billing.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_billing.types.error_message
    import aws_sdk_billing.types.validation_exception_field_list
    import aws_sdk_billing.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: "aws_sdk_billing.types.error_message.ErrorMessage"
    reason: (
        "aws_sdk_billing.types.validation_exception_reason.ValidationExceptionReason"
    )
    """<p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>"""
    field_list: NotRequired[
        "aws_sdk_billing.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_billing.types.validation_exception_reason

    out["reason"] = (
        aws_sdk_billing.types.validation_exception_reason.serialize_aws_json_1_0(
            value["reason"]
        )
    )
    if "field_list" in value:
        import aws_sdk_billing.types.validation_exception_field_list

        out["fieldList"] = (
            aws_sdk_billing.types.validation_exception_field_list.serialize_aws_json_1_0(
                value["field_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "reason" in data:
        import aws_sdk_billing.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_billing.types.validation_exception_reason.deserialize_aws_json_1_0(
                data["reason"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "fieldList" in data:
        import aws_sdk_billing.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_billing.types.validation_exception_field_list.deserialize_aws_json_1_0(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.billing#ValidationException``."""

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
    def from_aws_json_1_0(cls, data: dict) -> "ValidationException":
        return cls(deserialize_aws_json_1_0(data))
