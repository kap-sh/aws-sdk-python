"""Generated from Smithy shape ``com.amazonaws.interconnect#InterconnectValidationException``."""

from typing_extensions import TypedDict

from capo_interconnect.errors import DeserializationError, ServiceError


class InterconnectValidationException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InterconnectValidationException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InterconnectValidationException_:
    out: InterconnectValidationException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InterconnectValidationException_.message required")
    return out


class InterconnectValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.interconnect#InterconnectValidationException``."""

    code: str | None = "InterconnectValidationException"

    def __init__(self, data: InterconnectValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InterconnectValidationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InterconnectValidationException":
        return cls(deserialize_aws_json_1_0(data))
