"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvalidInputException``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, ServiceError


class InvalidInputException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidInputException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidInputException_:
    out: InvalidInputException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidInputException_.message required")
    return out


class InvalidInputException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#InvalidInputException``."""

    code: str | None = "InvalidInputException"

    def __init__(self, data: InvalidInputException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidInputException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidInputException":
        return cls(deserialize_json(data))
