"""Generated from Smithy shape ``com.amazonaws.rum#InvalidPolicyRevisionIdException``."""

from typing_extensions import TypedDict

from capo_rum.errors import DeserializationError, ServiceError


class InvalidPolicyRevisionIdException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidPolicyRevisionIdException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidPolicyRevisionIdException_:
    out: InvalidPolicyRevisionIdException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidPolicyRevisionIdException_.message required")
    return out


class InvalidPolicyRevisionIdException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rum#InvalidPolicyRevisionIdException``."""

    code: str | None = "InvalidPolicyRevisionIdException"

    def __init__(self, data: InvalidPolicyRevisionIdException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPolicyRevisionIdException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidPolicyRevisionIdException":
        return cls(deserialize_json(data))
