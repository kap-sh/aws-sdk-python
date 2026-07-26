"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#ChannelInsufficientPermission``."""

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail_data.errors import ServiceError


class ChannelInsufficientPermission_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelInsufficientPermission_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ChannelInsufficientPermission_:
    out: ChannelInsufficientPermission_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ChannelInsufficientPermission(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtraildata#ChannelInsufficientPermission``."""

    code: str | None = "ChannelInsufficientPermission"

    def __init__(self, data: ChannelInsufficientPermission_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ChannelInsufficientPermission",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ChannelInsufficientPermission":
        return cls(deserialize_json(data))
