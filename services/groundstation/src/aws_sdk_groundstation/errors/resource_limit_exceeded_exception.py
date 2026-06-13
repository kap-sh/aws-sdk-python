"""Generated from Smithy shape ``com.amazonaws.groundstation#ResourceLimitExceededException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import ServiceError


class ResourceLimitExceededException_(TypedDict):
    message: NotRequired["str"]
    parameter_name: NotRequired["str"]
    """<p>Name of the parameter that exceeded the resource limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "parameter_name" in value:
        out["parameterName"] = value["parameter_name"]
    return out


def deserialize_json(data: dict) -> ResourceLimitExceededException_:
    out: ResourceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "parameterName" in data:
        out["parameter_name"] = data["parameterName"]
    return out


class ResourceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.groundstation#ResourceLimitExceededException``."""

    code: str | None = "ResourceLimitExceededException"

    def __init__(self, data: ResourceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceLimitExceededException":
        return cls(deserialize_json(data))
