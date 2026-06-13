"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GrantFlowEntitlements420Exception``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import ServiceError


class GrantFlowEntitlements420Exception_(TypedDict):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: GrantFlowEntitlements420Exception_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> GrantFlowEntitlements420Exception_:
    out: GrantFlowEntitlements420Exception_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class GrantFlowEntitlements420Exception(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediaconnect#GrantFlowEntitlements420Exception``."""

    code: str | None = "GrantFlowEntitlements420Exception"

    def __init__(self, data: GrantFlowEntitlements420Exception_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GrantFlowEntitlements420Exception",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "GrantFlowEntitlements420Exception":
        return cls(deserialize_json(data))
