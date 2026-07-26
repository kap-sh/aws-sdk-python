"""Generated from Smithy shape ``com.amazonaws.s3vectors#KmsInvalidKeyUsageException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_s3vectors.types.exception_message


class KmsInvalidKeyUsageException_(TypedDict, closed=True):
    message: "capo_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: KmsInvalidKeyUsageException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KmsInvalidKeyUsageException_:
    out: KmsInvalidKeyUsageException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("KmsInvalidKeyUsageException_.message required")
    return out


class KmsInvalidKeyUsageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#KmsInvalidKeyUsageException``."""

    code: str | None = "KmsInvalidKeyUsageException"

    def __init__(self, data: KmsInvalidKeyUsageException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsInvalidKeyUsageException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "KmsInvalidKeyUsageException":
        return cls(deserialize_json(data))
