"""Generated from Smithy shape ``com.amazonaws.frauddetector#ConflictException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_frauddetector.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.string


class ConflictException_(TypedDict, closed=True):
    message: "aws_sdk_frauddetector.types.string.string"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.frauddetector#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ConflictException":
        return cls(deserialize_aws_json_1_1(data))
