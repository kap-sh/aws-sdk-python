"""Generated from Smithy shape ``com.amazonaws.rum#MalformedPolicyDocumentException``."""

from typing_extensions import TypedDict

from capo_rum.errors import DeserializationError, ServiceError


class MalformedPolicyDocumentException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: MalformedPolicyDocumentException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> MalformedPolicyDocumentException_:
    out: MalformedPolicyDocumentException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("MalformedPolicyDocumentException_.message required")
    return out


class MalformedPolicyDocumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rum#MalformedPolicyDocumentException``."""

    code: str | None = "MalformedPolicyDocumentException"

    def __init__(self, data: MalformedPolicyDocumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MalformedPolicyDocumentException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "MalformedPolicyDocumentException":
        return cls(deserialize_json(data))
