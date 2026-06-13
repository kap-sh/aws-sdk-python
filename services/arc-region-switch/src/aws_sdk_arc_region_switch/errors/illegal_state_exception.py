"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#IllegalStateException``."""

from typing import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError, ServiceError


class IllegalStateException_(TypedDict):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IllegalStateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IllegalStateException_:
    out: IllegalStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("IllegalStateException_.message required")
    return out


class IllegalStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.arcregionswitch#IllegalStateException``."""

    code: str | None = "IllegalStateException"

    def __init__(self, data: IllegalStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "IllegalStateException":
        return cls(deserialize_aws_json_1_0(data))
