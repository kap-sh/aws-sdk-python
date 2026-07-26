"""Generated from Smithy shape ``com.amazonaws.s3vectors#KmsNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_s3vectors.types.exception_message


class KmsNotFoundException_(TypedDict, closed=True):
    message: "capo_s3vectors.types.exception_message.ExceptionMessage"


# --- restJson1 ser/de ---
def serialize_json(value: KmsNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> KmsNotFoundException_:
    out: KmsNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("KmsNotFoundException_.message required")
    return out


class KmsNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.s3vectors#KmsNotFoundException``."""

    code: str | None = "KmsNotFoundException"

    def __init__(self, data: KmsNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KmsNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "KmsNotFoundException":
        return cls(deserialize_json(data))
