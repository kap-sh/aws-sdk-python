"""Generated from Smithy shape ``com.amazonaws.interconnect#InterconnectServerException``."""

from typing import TypedDict

from aws_sdk_interconnect.errors import DeserializationError, ServiceError


class InterconnectServerException_(TypedDict):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InterconnectServerException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InterconnectServerException_:
    out: InterconnectServerException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InterconnectServerException_.message required")
    return out


class InterconnectServerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.interconnect#InterconnectServerException``."""

    code: str | None = "InterconnectServerException"

    def __init__(self, data: InterconnectServerException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InterconnectServerException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InterconnectServerException":
        return cls(deserialize_aws_json_1_0(data))
