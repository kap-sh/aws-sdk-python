"""Generated from Smithy shape ``com.amazonaws.medialive#UnprocessableEntityException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_medialive.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_validation_error
    import aws_sdk_medialive.types.__string


class UnprocessableEntityException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The error message."""
    validation_errors: NotRequired[
        "aws_sdk_medialive.types.__list_of_validation_error.__listOfValidationError"
    ]
    """A collection of validation error responses."""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessableEntityException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "validation_errors" in value:
        import aws_sdk_medialive.types.__list_of_validation_error

        out["validationErrors"] = (
            aws_sdk_medialive.types.__list_of_validation_error.serialize_json(
                value["validation_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> UnprocessableEntityException_:
    out: UnprocessableEntityException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "validationErrors" in data:
        import aws_sdk_medialive.types.__list_of_validation_error

        out["validation_errors"] = (
            aws_sdk_medialive.types.__list_of_validation_error.deserialize_json(
                data["validationErrors"]
            )
        )
    return out


class UnprocessableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.medialive#UnprocessableEntityException``."""

    code: str | None = "UnprocessableEntityException"

    def __init__(self, data: UnprocessableEntityException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnprocessableEntityException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnprocessableEntityException":
        return cls(deserialize_json(data))
