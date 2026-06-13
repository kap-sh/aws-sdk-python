"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#IllegalArgumentException``."""

from typing import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError, ServiceError


class IllegalArgumentException_(TypedDict):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IllegalArgumentException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IllegalArgumentException_:
    out: IllegalArgumentException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("IllegalArgumentException_.message required")
    return out


class IllegalArgumentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.arcregionswitch#IllegalArgumentException``."""

    code: str | None = "IllegalArgumentException"

    def __init__(self, data: IllegalArgumentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IllegalArgumentException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "IllegalArgumentException":
        return cls(deserialize_aws_json_1_0(data))
