"""Generated from Smithy shape ``com.amazonaws.interconnect#InterconnectClientException``."""

from typing import TypedDict

from aws_sdk_interconnect.errors import DeserializationError, ServiceError


class InterconnectClientException_(TypedDict):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InterconnectClientException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InterconnectClientException_:
    out: InterconnectClientException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InterconnectClientException_.message required")
    return out


class InterconnectClientException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.interconnect#InterconnectClientException``."""

    code: str | None = "InterconnectClientException"

    def __init__(self, data: InterconnectClientException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InterconnectClientException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InterconnectClientException":
        return cls(deserialize_aws_json_1_0(data))
