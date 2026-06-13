"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.validation_exception_type


class ValidationException_(TypedDict):
    message: NotRequired["str"]
    validation_exception_type: NotRequired[
        "aws_sdk_mediapackagev2.types.validation_exception_type.ValidationExceptionType"
    ]
    """<p>The type of ValidationException.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "validation_exception_type" in value:
        import aws_sdk_mediapackagev2.types.validation_exception_type

        out["ValidationExceptionType"] = (
            aws_sdk_mediapackagev2.types.validation_exception_type.serialize_json(
                value["validation_exception_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ValidationExceptionType" in data:
        import aws_sdk_mediapackagev2.types.validation_exception_type

        out["validation_exception_type"] = (
            aws_sdk_mediapackagev2.types.validation_exception_type.deserialize_json(
                data["ValidationExceptionType"]
            )
        )
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediapackagev2#ValidationException``."""

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
