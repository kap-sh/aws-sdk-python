"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ServiceException``."""

from typing import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, ServiceError


class ServiceException_(TypedDict):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ServiceException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceException_:
    out: ServiceException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceException_.message required")
    return out


class ServiceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentcore#ServiceException``."""

    code: str | None = "ServiceException"

    def __init__(self, data: ServiceException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceException":
        return cls(deserialize_json(data))
