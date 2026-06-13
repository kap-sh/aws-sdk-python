"""Generated from Smithy shape ``com.amazonaws.qconnect#DependencyFailedException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import ServiceError


class DependencyFailedException_(TypedDict):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DependencyFailedException_:
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DependencyFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.qconnect#DependencyFailedException``."""

    code: str | None = "DependencyFailedException"

    def __init__(self, data: DependencyFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyFailedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DependencyFailedException":
        return cls(deserialize_json(data))
