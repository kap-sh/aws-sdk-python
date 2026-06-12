"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#ChannelUnsupportedSchema``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail_data.errors import ServiceError


class ChannelUnsupportedSchema_(TypedDict):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelUnsupportedSchema_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ChannelUnsupportedSchema_:
    out: ChannelUnsupportedSchema_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ChannelUnsupportedSchema(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtraildata#ChannelUnsupportedSchema``."""

    code: str | None = "ChannelUnsupportedSchema"

    def __init__(self, data: ChannelUnsupportedSchema_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ChannelUnsupportedSchema",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ChannelUnsupportedSchema":
        return cls(deserialize_json(data))
