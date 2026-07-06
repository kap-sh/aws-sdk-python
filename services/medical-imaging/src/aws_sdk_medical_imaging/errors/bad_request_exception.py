"""Generated from Smithy shape ``com.amazonaws.medicalimaging#BadRequestException``."""

from typing_extensions import TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError, ServiceError


class BadRequestException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BadRequestException_.message required")
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.medicalimaging#BadRequestException``."""

    code: str | None = "BadRequestException"

    def __init__(self, data: BadRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BadRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadRequestException":
        return cls(deserialize_json(data))
