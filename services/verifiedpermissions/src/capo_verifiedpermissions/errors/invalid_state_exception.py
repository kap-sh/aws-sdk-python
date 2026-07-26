"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#InvalidStateException``."""

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, ServiceError


class InvalidStateException_(TypedDict, closed=True):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidStateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidStateException_.message required")
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.verifiedpermissions#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(self, data: InvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "InvalidStateException":
        return cls(deserialize_aws_json_1_0(data))
