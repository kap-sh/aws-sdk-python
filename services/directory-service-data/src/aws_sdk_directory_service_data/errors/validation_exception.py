"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_directory_service_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_directory_service_data.types.exception_message
    import aws_sdk_directory_service_data.types.validation_exception_reason


class ValidationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_directory_service_data.types.exception_message.ExceptionMessage"
    ]
    reason: NotRequired[
        "aws_sdk_directory_service_data.types.validation_exception_reason.ValidationExceptionReason"
    ]
    """<p> Reason the request failed validation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "reason" in value:
        import aws_sdk_directory_service_data.types.validation_exception_reason

        out["Reason"] = (
            aws_sdk_directory_service_data.types.validation_exception_reason.serialize_json(
                value["reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Reason" in data:
        import aws_sdk_directory_service_data.types.validation_exception_reason

        out["reason"] = (
            aws_sdk_directory_service_data.types.validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.directoryservicedata#ValidationException``."""

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
