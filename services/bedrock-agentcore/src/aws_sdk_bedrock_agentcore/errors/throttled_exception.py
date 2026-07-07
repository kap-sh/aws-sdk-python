"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ThrottledException``."""

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, ServiceError


class ThrottledException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ThrottledException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottledException_:
    out: ThrottledException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ThrottledException_.message required")
    return out


class ThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#ThrottledException``."""

    code: str | None = "ThrottledException"

    def __init__(self, data: ThrottledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottledException":
        return cls(deserialize_json(data))
