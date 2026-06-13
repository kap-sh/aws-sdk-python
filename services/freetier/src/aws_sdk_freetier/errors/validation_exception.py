"""Generated from Smithy shape ``com.amazonaws.freetier#ValidationException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_freetier.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_freetier.types.generic_string


class ValidationException_(TypedDict):
    message: "aws_sdk_freetier.types.generic_string.GenericString"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationException_.message required")
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.freetier#ValidationException``."""

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
