"""Generated from Smithy shape ``com.amazonaws.launchwizard#ResourceLimitException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_launch_wizard.errors import ServiceError


class ResourceLimitException_(TypedDict):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLimitException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceLimitException_:
    out: ResourceLimitException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceLimitException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.launchwizard#ResourceLimitException``."""

    code: str | None = "ResourceLimitException"

    def __init__(self, data: ResourceLimitException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceLimitException":
        return cls(deserialize_json(data))
