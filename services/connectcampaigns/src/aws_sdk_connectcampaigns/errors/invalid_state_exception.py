"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#InvalidStateException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcampaigns.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.x_amazon_error_type


class InvalidStateException_(TypedDict):
    message: "str"
    x_amz_error_type: NotRequired[
        "aws_sdk_connectcampaigns.types.x_amazon_error_type.XAmazonErrorType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidStateException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidStateException_:
    out: InvalidStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidStateException_.message required")
    return out


class InvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectcampaigns#InvalidStateException``."""

    code: str | None = "InvalidStateException"

    def __init__(self, data: InvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidStateException":
        return cls(deserialize_json(data))
