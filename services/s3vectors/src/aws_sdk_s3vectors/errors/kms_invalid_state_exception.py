"""Generated from Smithy shape ``com.amazonaws.s3vectors#KmsInvalidStateException``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.exception_message


class KmsInvalidStateException_(TypedDict):
    message: "aws_sdk_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: KmsInvalidStateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KmsInvalidStateException_:
    out: KmsInvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("KmsInvalidStateException_.message required")
    return out


class KmsInvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#KmsInvalidStateException``."""

    code: str | None = "KmsInvalidStateException"

    def __init__(self, data: KmsInvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsInvalidStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "KmsInvalidStateException":
        return cls(deserialize_json(data))
