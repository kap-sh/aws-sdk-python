"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnprocessableEntityException``."""

from typing import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError, ServiceError


class UnprocessableEntityException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessableEntityException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnprocessableEntityException_:
    out: UnprocessableEntityException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("UnprocessableEntityException_.message required")
    return out


class UnprocessableEntityException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.accessanalyzer#UnprocessableEntityException``."""

    code: str | None = "UnprocessableEntityException"

    def __init__(self, data: UnprocessableEntityException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="UnprocessableEntityException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnprocessableEntityException":
        return cls(deserialize_json(data))
