"""Generated from Smithy shape ``com.amazonaws.networkmanager#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmanager.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.server_side_string
    import aws_sdk_networkmanager.types.validation_exception_field_list
    import aws_sdk_networkmanager.types.validation_exception_reason


class ValidationException_(TypedDict, closed=True):
    message: "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    reason: NotRequired[
        "aws_sdk_networkmanager.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p>The reason for the error.</p>"""
    fields: NotRequired[
        "aws_sdk_networkmanager.types.validation_exception_field_list.ValidationExceptionFieldList"
    ]
    """<p>The fields that caused the error, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_networkmanager.types.validation_exception_reason

        out["Reason"] = (
            aws_sdk_networkmanager.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    if "fields" in value:
        import aws_sdk_networkmanager.types.validation_exception_field_list

        out["Fields"] = (
            aws_sdk_networkmanager.types.validation_exception_field_list.serialize_json(
                value["fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    if "Reason" in data:
        import aws_sdk_networkmanager.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_networkmanager.types.validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    if "Fields" in data:
        import aws_sdk_networkmanager.types.validation_exception_field_list

        out["fields"] = (
            aws_sdk_networkmanager.types.validation_exception_field_list.deserialize_json(
                data["Fields"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.networkmanager#ValidationException``."""

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
