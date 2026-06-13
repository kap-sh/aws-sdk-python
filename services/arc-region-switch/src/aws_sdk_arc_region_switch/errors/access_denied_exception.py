"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AccessDeniedException``."""

from typing import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError, ServiceError


class AccessDeniedException_(TypedDict):
    message: "str"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.arcregionswitch#AccessDeniedException``."""

    code: str | None = "AccessDeniedException"

    def __init__(self, data: AccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_0(data))
