"""Generated from Smithy shape ``com.amazonaws.s3vectors#KmsDisabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_s3vectors.types.exception_message


class KmsDisabledException_(TypedDict, closed=True):
    message: "capo_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: KmsDisabledException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KmsDisabledException_:
    out: KmsDisabledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("KmsDisabledException_.message required")
    return out


class KmsDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#KmsDisabledException``."""

    code: str | None = "KmsDisabledException"

    def __init__(self, data: KmsDisabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsDisabledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "KmsDisabledException":
        return cls(deserialize_json(data))
