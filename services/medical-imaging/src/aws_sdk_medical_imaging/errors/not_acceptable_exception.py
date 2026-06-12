"""Generated from Smithy shape ``com.amazonaws.medicalimaging#NotAcceptableException``."""

from typing import TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError, ServiceError


class NotAcceptableException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: NotAcceptableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> NotAcceptableException_:
    out: NotAcceptableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("NotAcceptableException_.message required")
    return out


class NotAcceptableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.medicalimaging#NotAcceptableException``."""

    code: str | None = "NotAcceptableException"

    def __init__(self, data: NotAcceptableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotAcceptableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "NotAcceptableException":
        return cls(deserialize_json(data))
