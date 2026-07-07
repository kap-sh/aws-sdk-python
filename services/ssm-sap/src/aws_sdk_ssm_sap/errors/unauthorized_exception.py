"""Generated from Smithy shape ``com.amazonaws.ssmsap#UnauthorizedException``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_sap.errors import ServiceError


class UnauthorizedException_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: UnauthorizedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnauthorizedException_:
    out: UnauthorizedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnauthorizedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssmsap#UnauthorizedException``."""

    code: str | None = "UnauthorizedException"

    def __init__(self, data: UnauthorizedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnauthorizedException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnauthorizedException":
        return cls(deserialize_json(data))
