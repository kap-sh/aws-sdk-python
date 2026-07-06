"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_managed_integrations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.error_message


class ValidationException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_iot_managed_integrations.types.error_message.ErrorMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iotmanagedintegrations#ValidationException``."""

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
