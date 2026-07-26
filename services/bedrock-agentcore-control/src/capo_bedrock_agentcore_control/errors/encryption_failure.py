"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EncryptionFailure``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError, ServiceError


class EncryptionFailure_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionFailure_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EncryptionFailure_:
    out: EncryptionFailure_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("EncryptionFailure_.message required")
    return out


class EncryptionFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EncryptionFailure``."""

    code: str | None = "EncryptionFailure"

    def __init__(self, data: EncryptionFailure_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EncryptionFailure",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "EncryptionFailure":
        return cls(deserialize_json(data))
