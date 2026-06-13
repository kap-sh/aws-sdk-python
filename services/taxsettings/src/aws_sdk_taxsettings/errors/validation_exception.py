"""Generated from Smithy shape ``com.amazonaws.taxsettings#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_taxsettings.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.error_message
    import aws_sdk_taxsettings.types.validation_exception_error_code
    import aws_sdk_taxsettings.types.validation_exception_field_list


class ValidationException_(TypedDict):
    message: "aws_sdk_taxsettings.types.error_message.ErrorMessage"
    error_code: "aws_sdk_taxsettings.types.validation_exception_error_code.ValidationExceptionErrorCode"
    """<p>400</p>"""
    field_list: NotRequired[
        "aws_sdk_taxsettings.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>400</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_taxsettings.types.validation_exception_error_code

    out["errorCode"] = (
        aws_sdk_taxsettings.types.validation_exception_error_code.serialize_json(
            value["error_code"]
        )
    )
    if "field_list" in value:
        import aws_sdk_taxsettings.types.validation_exception_field_list

        out["fieldList"] = (
            aws_sdk_taxsettings.types.validation_exception_field_list.serialize_json(
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
    if "errorCode" in data:
        import aws_sdk_taxsettings.types.validation_exception_error_code

        out["error_code"] = (
            aws_sdk_taxsettings.types.validation_exception_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        raise DeserializationError("ValidationException_.error_code required")
    if "fieldList" in data:
        import aws_sdk_taxsettings.types.validation_exception_field_list

        out["field_list"] = (
            aws_sdk_taxsettings.types.validation_exception_field_list.deserialize_json(
                data["fieldList"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.taxsettings#ValidationException``."""

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
