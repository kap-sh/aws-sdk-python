"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain_query.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.exception_message
    import aws_sdk_managedblockchain_query.types.validation_exception_field_list
    import aws_sdk_managedblockchain_query.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "aws_sdk_managedblockchain_query.types.exception_message.ExceptionMessage"
    """<p>The container for the exception message.</p>"""
    reason: "aws_sdk_managedblockchain_query.types.validation_exception_reason.ValidationExceptionReason"
    """<p>The container for the reason for the exception</p>"""
    field_list: NotRequired[
        "aws_sdk_managedblockchain_query.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The container for the <code>fieldList</code> of the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    out["reason"] = value["reason"]
    if "field_list" in value:
        import aws_sdk_managedblockchain_query.types.validation_exception_field_list

        out["fieldList"] = (
            aws_sdk_managedblockchain_query.types.validation_exception_field_list.serialize_json(
                value["field_list"]
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
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("ValidationException_.reason required")
    if "fieldList" in data:
        import aws_sdk_managedblockchain_query.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_managedblockchain_query.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.managedblockchainquery#ValidationException``."""

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
