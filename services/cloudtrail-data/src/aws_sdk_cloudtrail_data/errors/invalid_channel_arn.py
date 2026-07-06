"""Generated from Smithy shape ``com.amazonaws.cloudtraildata#InvalidChannelARN``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail_data.errors import ServiceError


class InvalidChannelARN_(TypedDict, closed=True):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidChannelARN_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidChannelARN_:
    out: InvalidChannelARN_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidChannelARN(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtraildata#InvalidChannelARN``."""

    code: str | None = "InvalidChannelARN"

    def __init__(self, data: InvalidChannelARN_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidChannelARN",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidChannelARN":
        return cls(deserialize_json(data))
