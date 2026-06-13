"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.exception_message


class ValidationException_(TypedDict):
    message: "aws_sdk_ssm_incidents.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmincidents#ValidationException``."""

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
